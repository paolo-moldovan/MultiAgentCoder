import unittest
import subprocess
import os

# Path to your main.py file
MAIN_SCRIPT_PATH = os.path.join("src", "latest_ai_development", "main.py")

class TestMultiAgentCrew(unittest.TestCase):

    def test_run(self):
        """Test the 'run' function in main.py"""
        result = subprocess.run(
            ["python", MAIN_SCRIPT_PATH, "run"],
            capture_output=True,
            text=True
        )
        self.assertEqual(
            result.returncode, 0,
            f"'run' command failed with error:\n{result.stderr}"
        )

    def test_train(self):
        """Test the 'train' function in main.py (1 iteration for simplicity)"""
        result = subprocess.run(
            ["python", MAIN_SCRIPT_PATH, "train", "1", "test_output.json"],
            capture_output=True,
            text=True
        )
        self.assertEqual(
            result.returncode, 0,
            f"'train' command failed with error:\n{result.stderr}"
        )

    def test_replay(self):
        """
        Test the 'replay' function in main.py.
        Replace 'research_task' with a valid task ID if needed.
        """
        result = subprocess.run(
            ["python", MAIN_SCRIPT_PATH, "replay", "research_task"],
            capture_output=True,
            text=True
        )
        self.assertEqual(
            result.returncode, 0,
            f"'replay' command failed with error:\n{result.stderr}"
        )

    def test_test(self):
        """
        Test the 'test' function in main.py.
        We run it with 1 iteration using 'gpt-4' as the model name.
        """
        result = subprocess.run(
            ["python", MAIN_SCRIPT_PATH, "test", "1", "gpt-4"],
            capture_output=True,
            text=True
        )
        self.assertEqual(
            result.returncode, 0,
            f"'test' command failed with error:\n{result.stderr}"
        )

if __name__ == "__main__":
    unittest.main()