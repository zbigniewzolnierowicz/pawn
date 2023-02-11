import pytest
import sys
import os

if __name__ == "__main__":
    if os.path.isfile("test.db"):
        print("Detected an exisiting testing database - deleting it.")
        os.remove("test.db")
    sys.exit(pytest.main([]))
