

# Mood-Desktop-Local Ai

### A little clarity. A lot of possibility.

Mood is a Windows desktop AI assistant built for everyday questions, learning, brainstorming, and coding. It combines a clean conversational interface with locally running AI and optional neural speech.

Built with **Python, pywebview, Ollama, Kokoro ONNX, and SQLite**.

## Project Preview


https://github.com/user-attachments/assets/ec85b178-c9f5-466d-a6b9-8461f228ed08


## Why Mood?

Local AI tools can require terminal commands, separate applications, and manual configuration. Mood brings those components into one desktop application.

The goal is to make local AI more approachable: open the app, start a conversation, and keep useful answers organized.

Mood can help you:

- Understand a difficult concept through simpler explanations.
- Brainstorm ideas and turn them into practical plans.
- Work through programming questions with text and code attachments.
- Listen to responses using locally generated speech.
- Return to previous conversations without starting over.

The default configuration runs chat and speech locally after the initial downloads, without requiring a paid inference API.

## Features

| Feature | Description |
| --- | --- |
| Streaming responses | Read answers as the model generates them. |
| Saved conversations | Create, search, rename, and delete chats. |
| Text and code attachments | Add small UTF-8 files as context for a question. |
| Neural speech | Listen to replies using Kokoro’s `af_heart` voice. |
| Copy and export | Copy answers and code blocks, or export a conversation as text. |
| Appearance settings | Choose dark, light, or system appearance. |
| Custom instructions | Adjust the assistant’s behavior in settings. |
| Model settings | Choose an available Ollama model. |
| First-run setup | See model download progress and retry failed setup. |
| Windows packaging | Build a distributable desktop application with PyInstaller. |

The default language model is `llama2-uncensored`. The packaged executable starts with this preset.

## Technology Stack

| Technology | Purpose |
| --- | --- |
| Python | Application logic and background tasks |
| HTML, CSS, JavaScript | Desktop interface |
| pywebview | Native window and Python–JavaScript bridge |
| Ollama | Local language model runtime |
| Kokoro ONNX | Local neural speech synthesis |
| sounddevice | Audio playback |
| SQLite | Conversation and settings storage |
| PyInstaller | Windows application packaging |

## How It Works

1. The user sends a message, optionally including text or code attachments.
2. The Python backend combines the message with recent conversation context.
3. Ollama runs the selected model locally and streams its response.
4. The interface displays the answer while it is being generated.
5. The conversation is saved to SQLite.
6. If speech is enabled, Kokoro generates audio for the reply.

Mood reuses an available local Ollama server. Otherwise, it starts the bundled runtime and closes the process it owns when the app exits.

## Getting Started

### Requirements

- Windows 10 or Windows 11.
- Python 3.12, 64-bit, for running from source or building.
- Windows Python launcher.
- Microsoft Edge WebView2 Runtime.
- Internet access for initial downloads.
- Several GB of available storage for the language model, plus space for application dependencies.

Performance depends on the selected model and available hardware. CPU-only generation can be slower.

### Run From Source

Download and extract this repository, or clone it:

```bash
git clone https://github.com/Moodyger/mood-desktop-ai.git
cd mood-desktop-ai
```

Then:

1. Run `Setup_Mood.bat`.
2. Wait for dependencies, voice files, and the Ollama runtime to download.
3. Run `Run_Mood.bat`.
4. Keep Mood open while the language model downloads.
5. Start chatting when setup reports that it is ready.

Setup creates a separate `.venv_mood` environment. Other installed Python versions can remain on your computer.

### Example Prompts

> Explain recursion using a short Python example, then give me a practice question.

> Help me turn a desktop app idea into a small first version.

> Review this attached code and explain what I could improve.

## Build a Windows Application

After completing setup:

1. Run Mood and check that chat and speech work.
2. Close the application.
3. Run `Build_Mood.bat`.
4. Open the generated `dist/Mood/` folder.
5. ZIP the entire folder for distribution.

The complete distribution includes:

```text
dist/
└── Mood/
    ├── Mood.exe
    ├── _internal/
    ├── runtime/
    └── ...
```

**Keep the entire folder together. Sending only `Mood.exe` leaves out required dependencies.**

Recipients using the complete build do not need Python or a separate Ollama installation. They extract the folder and launch `Mood.exe`. The first launch requires internet access to download the language model.

WebView2 is still required. Test the complete build on another Windows computer before publishing a release.

## Project Structure

```text
techaid_io.py       Main application, interface, chat, storage, and speech
setup_mood.py      Dependency, voice asset, and runtime setup
build_mood.py      Windows build workflow
Check_Voice.py     Voice synthesis check
requirements.txt  Python dependencies
Setup_Mood.bat     Setup launcher
Run_Mood.bat       Application launcher
Build_Mood.bat     Build launcher
Mood.ico          Application icon
```

The main file retains its original `techaid_io.py` name from the project’s earlier branding.

## Local Data and Privacy

Conversations and settings are stored locally at:

```text
%LOCALAPPDATA%\TechAidIO\chats.sqlite3
```

- Language models use Ollama’s standard user model directory.
- Attached text is included in the prompt and saved with the conversation.
- Chat generation and speech run locally with the bundled configuration.
- Initial dependency, runtime, and model downloads require internet access.
- Local storage is not an encrypted vault; avoid attaching passwords or credentials.

## Current Limitations

- Windows is the intended platform; macOS and Linux packages are not provided.
- Attachments support UTF-8 text and code, not images, PDFs, or Word documents.
- A message accepts up to five files, totaling no more than 12,000 characters.
- Each attachment must be no larger than 100,000 bytes.
- Only limited recent conversation context is sent to the model.
- Response speed depends on hardware and model size.
- AI answers can be incorrect. The default uncensored model may also generate inappropriate content.
- `Check_Voice.py` checks speech synthesis; it is not a complete application test suite.

## Troubleshooting

| Problem | Suggested fix |
| --- | --- |
| Python 3.12 is not found | Install Python 3.12, 64-bit, with the Python launcher. |
| AI runtime is missing | Extract the full distribution and keep `runtime/` beside `Mood.exe`. |
| Model download fails | Check connectivity and available storage, then select **Retry setup**. |
| Voice files are missing | Rerun source setup or extract the complete packaged build. |
| Desktop interface does not open | Check that Microsoft Edge WebView2 Runtime is installed. |
| Downloaded DLL is blocked | If you trust the download, unblock the ZIP in Windows Properties and extract it again. |
| Replies are slow | Check available memory and allow extra time for CPU-only inference. |

## Roadmap

- [ ] Publish a Windows release tested on a second computer.
- [ ] Add a live walkthrough demonstrating chat and speech.
- [ ] Measure startup time and document hardware requirements.
- [ ] Add automated tests for storage, setup recovery, and response failures.
- [ ] Separate the interface, storage, model runtime, and speech into smaller modules.
- [ ] Improve accessibility and setup diagnostics.

## Project Scope and Credits

Mood is a custom desktop application integrating existing language and speech models. It does not train its own foundation model.

Development included AI-assisted coding and iteration. The project focuses on desktop interface design, local AI integration, persistent conversations, speech, and Windows distribution.

Thanks to the projects that make Mood possible:

- [Ollama](https://github.com/ollama/ollama)
- [llama2-uncensored](https://ollama.com/library/llama2-uncensored)
- [Kokoro](https://huggingface.co/hexgrad/Kokoro-82M)
- [kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx)
- [pywebview](https://pywebview.flowrl.com/)
- [PyInstaller](https://pyinstaller.org/)
- [Phonemizer](https://github.com/bootphon/phonemizer)
- [eSpeak NG](https://github.com/espeak-ng/espeak-ng)

## License

This repository does not currently declare a project-wide license.

Third-party libraries, runtimes, and model assets have their own licenses and terms. Review those requirements before redistribution.
