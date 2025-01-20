import unittest
import subprocess
import os
import sys

# Fix the path to point to the correct location
MAIN_SCRIPT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "src", "multi_agent_crew", "main.py")

class TestMultiAgentCrew(unittest.TestCase):
    def setUp(self):
        print(f"\nRunning test from: {os.getcwd()}")
        print(f"Main script path: {MAIN_SCRIPT_PATH}")
        print(f"Python executable: {sys.executable}")
        
    def run_command(self, command_args):
        print(f"\nExecuting command: {' '.join(command_args)}")
        result = subprocess.run(
            command_args,
            capture_output=True,
            text=True
        )
        
        print("\nCommand output:")
        if result.stdout:
            print(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            print(f"STDERR:\n{result.stderr}")
            
        print(f"Return code: {result.returncode}")
        return result

    def test_run(self):
        print("\n=== Testing RUN command ===")
        result = self.run_command(["python", MAIN_SCRIPT_PATH, "run"])
        self.assertEqual(
            result.returncode, 0,
            f"'run' command failed with return code {result.returncode}\nError:\n{result.stderr}"
        )

    def test_train(self):
        print("\n=== Testing TRAIN command ===")
        result = self.run_command([
            "python", 
            MAIN_SCRIPT_PATH, 
            "train", 
            "1", 
            "test_output.json"
        ])
        self.assertEqual(
            result.returncode, 0,
            f"'train' command failed with return code {result.returncode}\nError:\n{result.stderr}"
        )
        
        if os.path.exists("test_output.json"):
            print("Successfully created test_output.json")
        else:
            print("Warning: test_output.json was not created")

    def test_replay(self):
        print("\n=== Testing REPLAY command ===")
        result = self.run_command([
            "python", 
            MAIN_SCRIPT_PATH, 
            "replay", 
            "research_task"
        ])
        self.assertEqual(
            result.returncode, 0,
            f"'replay' command failed with return code {result.returncode}\nError:\n{result.stderr}"
        )

    def test_test(self):
        print("\n=== Testing TEST command ===")
        result = self.run_command([
            "python", 
            MAIN_SCRIPT_PATH, 
            "test", 
            "1", 
            "phi4"
        ])
        self.assertEqual(
            result.returncode, 0,
            f"'test' command failed with return code {result.returncode}\nError:\n{result.stderr}"
        )

    def tearDown(self):
        print("\nTest completed")
        if os.path.exists("test_output.json"):
            try:
                os.remove("test_output.json")
                print("Cleaned up test_output.json")
            except Exception as e:
                print(f"Warning: Could not clean up test_output.json: {e}")

if __name__ == "__main__":
    unittest.main(verbosity=2)