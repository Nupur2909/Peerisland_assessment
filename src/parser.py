from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path
from src.config import REPO_PATH, CHUNK_SIZE, CHUNK_OVERLAP
from src.utils import get_code_files

def parse_and_chunk_files():
    print("🔍 Parsing and chunking code...")
    file_paths = get_code_files(REPO_PATH)
    chunks = []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    for path in file_paths:
        try:
            loader = TextLoader(path, encoding='utf-8')
            documents = loader.load_and_split(text_splitter=splitter)
            chunks.extend(documents)
        except Exception as e:
            print(f"⚠️ Error loading {path}: {e}")

    print(f"✅ Parsed {len(chunks)} chunks.")
    return chunks
