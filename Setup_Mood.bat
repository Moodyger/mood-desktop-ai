@echo off
setlocal
cd /d "%~dp0"
py -3.12 --version
if errorlevel 1 (
 echo Python 3.12 was not found. Install Python 3.12 64-bit first.
 echo Your Python 3.15 installation can stay installed.
 pause
 exit /b 1
)
py -3.12 setup_mood.py
if errorlevel 1 (
 echo Setup did not finish. Send the error above for help.
 pause
 exit /b 1
)
echo Setup complete. Double-click Run_Mood.bat next.
pause
