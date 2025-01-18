from crewai import Agent
from models.llm_config import initialize_llm
from config.settings import AGENT_SETTINGS

class ResearcherAgent:
    def __init__(self):
        self.llm = initialize_llm()
        self.settings = AGENT_SETTINGS["researcher"]
        
    def create_agent(self):
        return Agent(
            role=self.settings["role"],
            goal=self.settings["goal"],
            backstory=self.settings["backstory"],
            llm=self.llm
        ) 