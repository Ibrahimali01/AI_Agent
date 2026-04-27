import unittest
from src.main import main
from io import StringIO
import sys

class TestMain(unittest.TestCase):
    def test_output(self):
        captured = StringIO()
        sys.stdout = captured
        main()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue().strip(), "Hello, Termux!")

if __name__ == "__main__":
    unittest.main()
