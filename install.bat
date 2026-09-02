@echo off
REM Installation script for KWOLI TOOL
echo.
echo ======================================
echo  KWOLI TOOL - Installation Script
echo ======================================
echo.

echo Installing dependencies...
pip install -r kwoli_tool\requirements.txt

echo.
echo ======================================
echo Installation complete!
echo.
echo To run the application, execute:
echo   python run.py
echo ======================================
echo.
pause
