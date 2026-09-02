#!/usr/bin/env python3
"""
KWOLI TOOL Launcher
Запустите этот файл для начала работы приложения
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from kwoli_tool.main import main

if __name__ == "__main__":
    main()
