from crewai import Task
from utils.task_tracker import TaskTracker

class TaskDefinitions:
    def __init__(self, researcher, coder, reviewer):
        self.researcher = researcher
        self.coder = coder
        self.reviewer = reviewer
        self.task_tracker = TaskTracker()

    def get_research_task(self, context):
        return Task(
            description=f"Research coding standards and best practices for: {context}",
            expected_output="Detailed research findings including best practices, design patterns, and implementation recommendations",
            agent=self.researcher,
            callback=self.task_tracker.track_progress
        )

    def get_coding_task(self, research_output):
        return Task(
            description=f"Generate code based on the following research: {research_output}",
            expected_output="Complete, working code implementation following the research findings",
            agent=self.coder,
            callback=self.task_tracker.track_progress
        )

    def get_review_task(self, code):
        return Task(
            description=f"Review and suggest improvements for the following code: {code}",
            expected_output="Code review with specific improvement suggestions and explanations",
            agent=self.reviewer,
            callback=self.task_tracker.track_progress
        ) 