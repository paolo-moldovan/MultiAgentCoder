# Multi-Agent Crew

A multi-agent system for collaborative software development using CrewAI. This system orchestrates multiple AI agents to work together on software development tasks, from research to implementation and review.

## Project Structure

    src/
    └── multi_agent_crew/
        ├── config/
        │   ├── agents.yaml    # Agent configurations
        │   └── tasks.yaml     # Task definitions
        ├── tools/             # Custom tools for agents
        ├── crew.py           # Main crew implementation
        └── main.py           # CLI entry point
    tests/                    # Test suite
    LICENSE                   # MIT License
    requirements.txt          # Project dependencies

## Agents

The system includes the following specialized agents:

1. Research Specialist: Researches and analyzes requirements
2. Reporting Analyst: Creates comprehensive technical documentation
3. Crew Captain: Coordinates team efforts and manages project flow
4. System Architect: Designs system architecture
5. Frontend Developer: Implements user interfaces
6. Backend Developer: Implements server-side logic
7. DevOps Engineer: Sets up infrastructure and deployment pipelines
8. QA Specialist: Ensures quality through testing
9. Code Reviewer: Reviews and improves code quality

## Tasks

The system executes the following tasks in sequence:

1. Research Task: Initial research and requirement analysis
2. Reporting Task: Documentation generation (outputs to report.md)
3. Crew Management Task: Project coordination
4. Architecture Planning Task: System design
5. Frontend Implementation Task: UI development
6. Backend Development Task: Server-side implementation
7. DevOps Pipeline Task: Infrastructure setup
8. Quality Assurance Task: Testing and validation
9. Code Review Task: Code quality review

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses UV (https://docs.astral.sh/uv/) for dependency management.

Install UV if you haven't already:
pip install uv

Clone the repository:
git clone <repository-url>
cd multi-agent-crew

Install dependencies using UV:
uv pip install -r requirements.txt

Make sure you have Ollama installed and running
Pull the required model:
ollama pull codestral

## Configuration

### Environment Setup
Create a .env file in the root directory:

OLLAMA_BASE_URL=http://localhost:11434

### Customizing Agents and Tasks
- Modify src/multi_agent_crew/config/agents.yaml to define your agents
- Modify src/multi_agent_crew/config/tasks.yaml to define your tasks
- Modify src/multi_agent_crew/crew.py to add custom logic and tools
- Modify src/multi_agent_crew/main.py to customize inputs

## Usage

The system provides several command-line interfaces:

Run the crew:
python src/multi_agent_crew/main.py run

Train the crew (specify iterations and output file):
python src/multi_agent_crew/main.py train <iterations> <output-file>

Replay a specific task:
python src/multi_agent_crew/main.py replay <task-id>

Run tests:
python src/multi_agent_crew/main.py test <iterations> <model-name>

### Example

Run a basic development workflow:
python src/multi_agent_crew/main.py run

This will execute a complete workflow where agents collaborate to:
1. Research and analyze requirements
2. Generate technical documentation
3. Plan architecture
4. Implement frontend and backend components
5. Set up infrastructure
6. Perform testing and code review

## Testing

Run the test suite:
python -m unittest tests/test_crew.py -v

## Output

- Task results are printed to console
- Technical reports are saved to report.md
- Training data is saved to specified JSON files

## Requirements

- Python >=3.10 <3.13
- CrewAI >=0.11.0
- Langchain >=0.1.0
- Ollama with codestral model
- UV package manager

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add some amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

## Support

For support, questions, or feedback:
- Create an issue in the GitHub repository
- Visit CrewAI documentation: https://docs.crewai.com
- Join the CrewAI Discord: https://discord.com/invite/X4JWnZnxPb

Let's create wonders together with the power and simplicity of crewAI.
