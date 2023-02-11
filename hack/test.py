import sys
from pathlib import Path

import pytest

if __name__ == "__main__":
    if Path("test.db").is_file():
        print("Detected an exisiting testing database - deleting it.")
        Path("test.db").unlink()
    sys.exit(pytest.main([]))
