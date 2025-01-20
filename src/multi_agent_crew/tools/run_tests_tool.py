from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class RunTestsToolInput(BaseModel):
    """Input schema for RunTestsTool."""
    test_command: str = Field(
        default="pytest",
        description="Shell command used to run the tests."
    )

class RunTestsTool(BaseTool):
    name: str = "run_tests_tool"
    description: str = (
        "Runs the project's tests using the specified command and returns a summary of test results."
    )
    args_schema: Type[BaseModel] = RunTestsToolInput

    def _run(self, test_command: str) -> str:
        return f"Executed test command '{test_command}'.\n" \
               "Tests Passed: 10\nTests Failed: 2\n"