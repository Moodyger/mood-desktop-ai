@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv_mood\Scripts\python.exe" goto missing
if not exist "voices\kokoro-v1.0.onnx" goto missing
if not exist "voices\voices-v1.0.bin" goto missing
".venv_mood\Scripts\python.exe" build_mood.py
if errorlevel 1 goto failed
start "" "%CD%\dist"
pause
exit /b 0
:missing
echo Run Setup_Mood.bat before building.
pause
exit /b 1
:failed
echo Build failed. Send the error shown above for help.
pause
exit /b 1
