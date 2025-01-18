from langchain_community.llms.ollama import Ollama

def initialize_llm():
    try:
        return Ollama(
            model="mistral",
            base_url="http://localhost:11434"
        )
    except Exception as e:
        raise Exception(f"Failed to initialize LLM: {str(e)}") 