from crewai import Agent
from langchain_community.llms import Ollama

class CoderAgent:
    def __init__(self):
        self.llm = Ollama(model="mistral")
        
    def create_agent(self):
        return Agent(
            role="Coder",
            goal="Generate efficient and maintainable code",
            backstory="Experienced software developer with expertise in multiple languages",
            llm=self.llm,
            verbose=True
        ) 