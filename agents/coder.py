from crewai import Agent
from models.llm_config import initialize_llm
from config.settings import AGENT_SETTINGS

class CoderAgent:
    def __init__(self):
        self.llm = initialize_llm()
        self.settings = AGENT_SETTINGS["coder"]
        
    def create_agent(self):
        """Create and return a coder agent."""
        return Agent(
            role=self.settings["role"],
            goal=self.settings["goal"],
            backstory=self.settings["backstory"],
            llm=self.llm
        ) 