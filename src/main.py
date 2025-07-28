from src.parser import parse_and_chunk_files
from src.summarizer import summarize_chunks



if __name__ == "__main__":
    # Step 1: Parse and chunk code files
    chunks = parse_and_chunk_files()

    # Step 2: Summarize code using Ollama
    summarize_chunks(chunks)
