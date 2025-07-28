import json5
import os
import json
import re
from tqdm import tqdm
import requests

from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL, OUTPUT_FILE
from langchain.schema import Document

def call_ollama_model(prompt: str):
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            headers={"Content-Type": "application/json"},
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=120  # ⏱️ Increase timeout for long generations
        )

        raw = response.text

        if "<html" in raw.lower():
            print("❌ HTML content received instead of JSON.")
            return None

        response_json = json5.loads(raw)
        return response_json.get("response", "").strip()

    except Exception as e:
        print(f"❌ Error summarizing with Ollama: {e}")
        return None

def extract_json_from_response(response):
    if not response:
        print("❌ No JSON found in response.")
        return None

    try:
        # Find first {...} JSON block using non-greedy match
        match = re.search(r'\{.*?\}', response, re.DOTALL)
        if match:
            json_str = match.group(0)
            return json5.loads(json_str)
        else:
            print("❌ Failed to extract JSON: No match found.")
            return None
    except Exception as e:
        print(f"❌ Failed to extract JSON: {e}")
        return None

def summarize_chunks(chunks: list[Document]):
    summaries = []

    print(f"🤖 Sending chunks to LLM for summarization...")
    for i, chunk in enumerate(tqdm(chunks, desc="🔍 Summarizing code chunks")):
        prompt = f"""
You are a helpful assistant. Summarize the following code chunk in JSON format with the following structure:
{{
  "summary": "...",
  "keywords": ["..."]
}}
Return ONLY valid JSON. Do NOT include markdown, backticks, or explanations.

Code:
{chunk.page_content}
"""

        raw_response = call_ollama_model(prompt)
        json_result = extract_json_from_response(raw_response)

        if json_result:
            summaries.append(json_result)
        else:
            print(f"⚠️ Failed to parse JSON for chunk #{i+1}")

    # Save to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(summaries, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved {len(summaries)} summaries to {OUTPUT_FILE}")
    return summaries
