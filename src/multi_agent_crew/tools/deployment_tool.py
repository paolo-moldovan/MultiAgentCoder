from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class DeploymentToolInput(BaseModel):
    environment: str = Field(..., description="The environment to deploy to (e.g., staging, production).")
    version_tag: str = Field(..., description="Version or release tag to deploy.")

class DeploymentTool(BaseTool):
    name: str = "deployment_tool"
    description: str = (
        "Deploys the application to the specified environment with a given version tag."
    )
    args_schema: Type[BaseModel] = DeploymentToolInput

    def _run(self, environment: str, version_tag: str) -> str:
        return (
            f"Deploying version '{version_tag}' to '{environment}' environment.\n"
            "Deployment complete! [stubbed result]"
        )