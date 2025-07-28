# 🧠 Code Summariser with Ollama + LangChain

This project automatically summarizes source code files using LLMs via [Ollama](https://ollama.com/) and [LangChain](https://www.langchain.com/). It recursively parses code, chunks it, and sends it to a local LLM running with Ollama, then saves structured JSON summaries.

---

## 🚀 Features

- ✅ Parse and chunk source code files
- ✅ Summarize each chunk using a local Ollama LLM (e.g., Mistral, Llama3)
- ✅ Output structured JSON summaries
- ✅ Robust error handling for malformed JSON
- ✅ Supports `.py`, `.java`, `.js`, `.ts`, `.cpp`, `.c`, `.cs`, `.go`, etc.

---

## 🛠️ Requirements

- Python 3.8+
- Ollama installed and running locally on port `11434`
- Git (for version control)

### 🔧 Install Dependencies

```bash
#pip install -r requirements.txt
