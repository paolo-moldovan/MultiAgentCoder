from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class MultiAgentCrew():
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    #
    # ----- AGENTS -----
    #
    
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )

    @agent
    def crew_captain(self) -> Agent:
        return Agent(
            config=self.agents_config['crew_captain'],
            verbose=True
        )

    @agent
    def system_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['system_architect'],
            verbose=True
        )

    @agent
    def frontend_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_developer'],
            verbose=True
        )

    @agent
    def backend_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['backend_developer'],
            verbose=True
        )

    @agent
    def devops_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['devops_engineer'],
            verbose=True
        )

    @agent
    def qa_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_specialist'],
            verbose=True
        )

    @agent
    def code_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['code_reviewer'],
            verbose=True
        )

    #
    # ----- TASKS -----
    #

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='report.md'
        )

    @task
    def crew_management_task(self) -> Task:
        return Task(
            config=self.tasks_config['crew_management_task'],
        )

    @task
    def architecture_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['architecture_planning_task'],
        )

    @task
    def frontend_implementation_task(self) -> Task:
        return Task(
            config=self.tasks_config['frontend_implementation_task'],
        )

    @task
    def backend_development_task(self) -> Task:
        return Task(
            config=self.tasks_config['backend_development_task'],
        )

    @task
    def devops_pipeline_task(self) -> Task:
        return Task(
            config=self.tasks_config['devops_pipeline_task'],
        )

    @task
    def quality_assurance_task(self) -> Task:
        return Task(
            config=self.tasks_config['quality_assurance_task'],
        )

    @task
    def code_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_review_task'],
        )

    #
    # ----- CREW DEFINITION -----
    #
    @crew
    def crew(self) -> Crew:
        """
        Creates the MultiAgentCrew.
        Adjust `process` (e.g., sequential, parallel, hierarchical) based on your needs.
        """
        return Crew(
            agents=self.agents,     # Agents automatically gathered by @agent
            tasks=self.tasks,       # Tasks automatically gathered by @task
            process=Process.sequential,
            verbose=True,
        )