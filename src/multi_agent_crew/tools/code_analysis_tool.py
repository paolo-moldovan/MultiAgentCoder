from crewai.tools import BaseTool
from typing import Type, Optional
from pydantic import BaseModel, Field

class CodeAnalysisToolInput(BaseModel):
    """Input schema for CodeAnalysisTool."""
    code_snippet: str = Field(..., description="The code snippet to analyze.")
    analysis_type: Optional[str] = Field(
        "complexity",
        description="The type of analysis to perform (e.g., 'complexity', 'lint', 'vulnerabilities')."
    )

class CodeAnalysisTool(BaseTool):
    name: str = "code_analysis_tool"
    description: str = (
        "Analyzes code snippets or files for complexity, style issues, or vulnerabilities."
    )
    args_schema: Type[BaseModel] = CodeAnalysisToolInput

    def _run(self, code_snippet: str, analysis_type: str = "complexity") -> str:
        return (
            f"Analysis Type: {analysis_type}\n"
            f"Snippet: {code_snippet[:60]}...\n"
            "Result: Complexity ~5, no style or security issues found (stub)."
        )