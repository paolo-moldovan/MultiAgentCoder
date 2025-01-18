from crewai import Crew, Process
from agents.researcher import ResearcherAgent
from agents.coder import CoderAgent
from agents.reviewer import ReviewerAgent
from tasks.task_definitions import TaskDefinitions
from utils.error_handler import handle_errors

class MultiAgentCoder:
    def __init__(self):
        self.researcher = ResearcherAgent().create_agent()
        self.coder = CoderAgent().create_agent()
        self.reviewer = ReviewerAgent().create_agent()
        
        self.task_definitions = TaskDefinitions(
            self.researcher,
            self.coder,
            self.reviewer
        )

    @handle_errors
    def process_coding_request(self, context):
        research_task = self.task_definitions.get_research_task(context)
        coding_task = self.task_definitions.get_coding_task("{research_output}")
        review_task = self.task_definitions.get_review_task("{code}")

        crew = Crew(
            agents=[self.researcher, self.coder, self.reviewer],
            tasks=[research_task, coding_task, review_task],
            process=Process.sequential
        )

        return crew.run()

if __name__ == "__main__":
    agent_coder = MultiAgentCoder()
    result = agent_coder.process_coding_request(
        "Create a simple REST API using FastAPI"
    )
    print(result) 