#!/bin/bash
# Installation script for KWOLI TOOL (Linux/Mac)

echo ""
echo "======================================"
echo "  KWOLI TOOL - Installation Script"
echo "======================================"
echo ""

echo "Installing dependencies..."
pip install -r kwoli_tool/requirements.txt

echo ""
echo "======================================"
echo "Installation complete!"
echo ""
echo "To run the application, execute:"
echo "  python run.py"
echo "or"
echo "  python3 run.py"
echo "======================================"
echo ""
