from langchain_community.llms import Ollama
from config.settings import OLLAMA_MODEL, OLLAMA_BASE_URL

def initialize_llm():
    try:
        return Ollama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_BASE_URL
        )
    except Exception as e:
        raise Exception(f"Failed to initialize LLM: {str(e)}") 