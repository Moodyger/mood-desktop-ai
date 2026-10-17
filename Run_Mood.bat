@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv_mood\Scripts\python.exe" (
 echo Run Setup_Mood.bat first.
 pause
 exit /b 1
)
".venv_mood\Scripts\python.exe" techaid_io.py
if errorlevel 1 pause
