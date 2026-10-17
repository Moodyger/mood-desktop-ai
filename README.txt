MOOD - COMPLETE FRIENDS AND FAMILY FOLDER

FOR YOU (BUILD ON WINDOWS)
1. Extract this source/setup ZIP into a folder outside your old Mood folder.
2. Install Python 3.12 64-bit if needed. Python 3.15 stays installed.
3. Run Setup_Mood.bat. It downloads Kokoro voice files and the official
   standalone Ollama Windows runtime. Downloads can be large.
4. Run Run_Mood.bat to test the app, then close Mood.
5. Run Build_Mood.bat. It builds dist/Mood/Mood.exe and copies the full
   Ollama runtime into dist/Mood/runtime. It also includes Kokoro speech.
   Existing users who already ran setup can run the new Build_Mood.bat;
   it downloads the runtime automatically if needed.
6. Zip the ENTIRE Mood folder inside dist and send that ZIP.
   Do not send this source/setup ZIP. Do not send only Mood.exe.
7. If you share via USB, copy the entire dist/Mood folder.

FOR YOUR FRIENDS (NO TECHNICAL SETUP)
1. Extract the ZIP you sent them.
2. Open Mood.exe.
3. Keep Mood open and connected to the internet while it downloads the
   llama2-uncensored model automatically. A progress message is shown.
4. When Mood says it is ready, start chatting.
No Python, terminal commands, pip, or separate Ollama installation needed.
The first setup needs several GB of free disk space and internet access.
Later launches reuse the model saved on that computer. The model is stored
in the user's standard Ollama model directory, not beside the exe.
WebView2 Runtime is needed for the desktop UI and is normally already on
Windows 10/11. If missing, install the Microsoft runtime from:
https://developer.microsoft.com/microsoft-edge/webview2/

BEHAVIOR
- Replies: llama2-uncensored. Voice: Kokoro Heart (af_heart).
- The exe starts with the requested Llama preset, even after older settings.
- Mood reuses an existing Ollama server where available. Otherwise it starts
  the included runtime on loopback port 11435 and stops its own server on exit.
- Download failures show an error and a Retry setup button.
- Chats/settings stay at LOCALAPPDATA/TechAidIO/chats.sqlite3.
- Keep runtime and _internal folders with Mood.exe.
- Close existing Mood windows before rebuilding/replacing files.
- CPU-only computers can generate replies more slowly.
- Windows playback, runtime download and exe building must be tested on your
  PC. They could not be executed in the Linux preparation workspace.

SOURCES / COMPONENTS
Ollama: https://github.com/ollama/ollama
Standalone runtime: https://github.com/ollama/ollama/releases
Kokoro weights: https://huggingface.co/hexgrad/Kokoro-82M
ONNX voice runtime: https://github.com/thewh1teagle/kokoro-onnx
Phonemizer: https://github.com/bootphon/phonemizer
Speech library: https://github.com/espeak-ng/espeak-ng
Desktop UI: https://pywebview.flowrl.com/
Packaging: https://pyinstaller.org/
