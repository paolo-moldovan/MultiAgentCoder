#!/usr/bin/env python
import sys
import warnings

# Fix the import path
from crew import MultiAgentCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Create a FastAPI application',
        'requirements': [
            'User authentication',
            'Database integration',
            'API documentation'
        ]
    }
    crew = MultiAgentCrew().crew()
    result = crew.kickoff(inputs=inputs)
    print("\nFinal Result:", result)

def train():
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        MultiAgentCrew().crew().train(
            n_iterations=int(sys.argv[2]),
            filename=sys.argv[3],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    try:
        MultiAgentCrew().crew().replay(
            task_id=sys.argv[2]
        )
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        MultiAgentCrew().crew().test(
            n_iterations=int(sys.argv[2]),
            openai_model_name=sys.argv[3],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify a command: run, train, replay, or test")
        sys.exit(1)
        
    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        print("Available commands: run, train, replay, test")
        sys.exit(1)