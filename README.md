# 🧠 Code Summarizer using LLMs (Ollama)

This project is a **code summarization pipeline** that parses source code files, splits them into logical chunks, and uses a **local LLM (like Ollama's Mistral)** to generate concise, structured summaries for each code chunk. Summaries are saved in JSON format for further usage like documentation, code review assistance, or onboarding new developers.

---

## 🚀 Features

- 📁 Parses and tokenizes source code files.
- 🔍 Chunks code intelligently for LLM processing.
- 🤖 Summarizes using a locally running Ollama LLM model (e.g., `mistral`, `codellama`).
- ✅ Saves output in `structured_summary.json`.
- 📉 Shows summarization progress with error handling and retries.
- 🧪 Designed with modular and scalable architecture.

---

## 📌 Approach

1. **Parsing**:
   - The codebase is recursively parsed using `langchain.document_loaders.TextLoader` to read `.java`, `.py`, `.js`, etc. files.

2. **Chunking**:
   - Code is split using `RecursiveCharacterTextSplitter` based on configured `CHUNK_SIZE` and `CHUNK_OVERLAP`.

3. **Prompting the LLM**:
   - For each chunk, a structured prompt is created to guide the model to respond in **valid JSON** format with keys like `"functionality"`, `"dependencies"`, `"summary"`, etc.

4. **LLM Summarization**:
   - Prompts are passed to Ollama's local API at `http://localhost:11434` using a lightweight POST request.
   - The raw output is parsed using `json5` to handle minor JSON format issues and ensure flexibility.

5. **Output Saving**:
   - All valid JSON summaries are saved to `structured_summary.json`.

---

## 🧠 Methodologies & Best Practices

- **Local LLM (Ollama)**: Avoids OpenAI API costs, ensures offline processing, and supports customizable models like `codellama`.
- **Prompt Engineering**: Prompts guide the LLM to follow structure and consistency.
- **Chunk Overlap**: Improves context preservation between adjacent code blocks.
- **Retries & Timeout Handling**: Improves robustness in case of LLM errors or timeouts.
- **Regex & Content Check**: Ensures HTML/error responses are skipped.
- **Error Logging**: Invalid JSONs or malformed responses are logged per chunk for debugging.

---

## ⚙️ Configuration

The config parameters can be found in `src/config.py`:

```python
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
OLLAMA_MODEL = "mistral"
OLLAMA_BASE_URL = "http://localhost:11434"
OUTPUT_FILE = "structured_summary.json"
