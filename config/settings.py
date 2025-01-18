OLLAMA_MODEL = "openhermes"
OLLAMA_BASE_URL = "http://localhost:11434"

AGENT_SETTINGS = {
    "researcher": {
        "role": "Researcher",
        "goal": "Gather coding best practices and relevant information",
        "backstory": "Expert in software development research and best practices"
    },
    "coder": {
        "role": "Coder",
        "goal": "Generate efficient and maintainable code",
        "backstory": "Experienced software developer with expertise in multiple languages"
    },
    "reviewer": {
        "role": "Reviewer",
        "goal": "Review and improve code quality",
        "backstory": "Senior developer specialized in code review and optimization"
    }
}

TASK_TIMEOUT = 300 