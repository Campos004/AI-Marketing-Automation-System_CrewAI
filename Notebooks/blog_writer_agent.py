from Demos.service.pipeTestServiceClient import verbose
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

from crewai_tools import TavilySearchTool, ScrapeWebsiteTool, DirectoryReadTool, FileWriterTool, FileReadTool

from dotenv import load_dotenv
load_dotenv()

@CrewBase
class BlogCrew():
    """" Blog writing Class """
    agents_config="config/agents.yaml"
    tasks_config="config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['research_agent'], #type:ignore[index]
            tools=[TavilySearchTool()],
            verbose=True
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer_agent'], #type:ignore[index]
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], #type:ignore[index]
            agent=self.researcher()
        )

    @task
    def writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['writer_task'], #type:ignore[index]
            agent=self.writer()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.researcher(),self.writer()],
            tasks=[self.research_task(),self.writer_task()]
        )

if __name__ == "__main__":
    blog_crew=BlogCrew()
    blog_crew.crew().kickoff(inputs={"topic":"The future of electrical vehicles"})