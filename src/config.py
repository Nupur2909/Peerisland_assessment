# ------------------------
# ✅ Model & API settings
# ------------------------

# Use only Ollama
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "phi"  # Or "llama3", "mistral", "codellama", etc. depending on what you installed
TEMPERATURE = 0.3

# ------------------------
# ✅ Data and Chunking
# ------------------------

REPO_PATH = "data/sakila_repo"   # Path to your local code repo
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# ------------------------
# ✅ Output
# ------------------------

OUTPUT_FILE = "output/structured_summary.json"
