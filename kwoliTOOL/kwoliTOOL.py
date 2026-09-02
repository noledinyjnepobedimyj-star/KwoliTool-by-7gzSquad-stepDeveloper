"""
Visual Studio startup file for KWOLI TOOL.
Launches the real application from the repository root.
"""

import os
import sys

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.chdir(_REPO_ROOT)

from kwoli_tool.main import main

if __name__ == "__main__":
    main()
