from crewai import Agent
from langchain_community.llms import Ollama

class ResearcherAgent:
    def __init__(self):
        self.llm = Ollama(model="mistral")
        
    def create_agent(self):
        return Agent(
            role="Researcher",
            goal="Research and analyze coding requirements",
            backstory="Expert in software development research and best practices",
            llm=self.llm,
            verbose=True
        ) 