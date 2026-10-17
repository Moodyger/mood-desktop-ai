"""Install into a private Python 3.12 environment and download local voice assets."""
import os
from pathlib import Path
import subprocess
import sys
import urllib.request
import venv
import shutil
import tempfile
import zipfile
from pathlib import PurePosixPath

ROOT = Path(__file__).resolve().parent
RELEASE = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.1/"

def prepare_runtime():
    """Bundle the official standalone runtime for recipients; no installer needed."""
    runtime = ROOT / 'runtime'
    if (runtime / 'ollama.exe').is_file() and (runtime / '.mood-runtime-complete').is_file():
        print('Bundled Ollama runtime is ready.', flush=True)
        return
    url = 'https://github.com/ollama/ollama/releases/latest/download/ollama-windows-amd64.zip'
    print('Downloading the official Ollama runtime. This large download is done on your PC before sharing.', flush=True)
    with tempfile.TemporaryDirectory(prefix='mood-runtime-') as work:
        archive = Path(work) / 'ollama.zip'
        downloaded = 0
        checkpoint = 0
        with urllib.request.urlopen(url, timeout=180) as response, archive.open('wb') as output:
            total = int(response.headers.get('Content-Length', 0))
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                output.write(chunk)
                downloaded += len(chunk)
                if downloaded - checkpoint >= 100 * 1024 * 1024:
                    print(f'  Ollama: {downloaded // (1024*1024)} MB downloaded', flush=True)
                    checkpoint = downloaded
        if total and downloaded != total:
            raise RuntimeError('The Ollama download was interrupted. Run the build again.')
        extracted = Path(work) / 'extracted'
        with zipfile.ZipFile(archive) as package:
            for member in package.infolist():
                relative = PurePosixPath(member.filename.replace(chr(92), '/'))
                if relative.is_absolute() or '..' in relative.parts or any(':' in part for part in relative.parts):
                    raise RuntimeError('Invalid runtime archive path.')
            if package.testzip() is not None:
                raise RuntimeError('The runtime archive is damaged. Run the build again.')
            package.extractall(extracted)
        candidates = list(extracted.rglob('ollama.exe'))
        if len(candidates) != 1:
            raise RuntimeError('Could not find Ollama in the official runtime archive.')
        source = candidates[0].parent
        runtime.mkdir(exist_ok=True)
        shutil.copytree(source, runtime, dirs_exist_ok=True)
        (runtime / '.mood-runtime-complete').write_text(url + '\n', encoding='utf-8')
    print('Ollama runtime bundled successfully.', flush=True)


def main():
    if sys.version_info[:2] != (3, 12):
        raise RuntimeError("Run this with Python 3.12 using Setup_Mood.bat.")
    folder = ROOT / ".venv_mood"
    python = folder / "Scripts" / "python.exe"
    if not python.is_file():
        print("Creating Mood's isolated Python environment...", flush=True)
        venv.EnvBuilder(with_pip=True).create(folder)
    subprocess.run([str(python), "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([str(python), "-m", "pip", "install", "-r", str(ROOT / "requirements.txt")], check=True)
    voices = ROOT / "voices"
    voices.mkdir(exist_ok=True)
    for name in ("kokoro-v1.0.onnx", "voices-v1.0.bin"):
        target = voices / name
        if target.is_file() and target.stat().st_size > 1_000_000:
            print("Already downloaded:", name, flush=True)
            continue
        temporary = target.with_suffix(target.suffix + ".part")
        print("Downloading", name, "(first setup only)...", flush=True)
        with urllib.request.urlopen(RELEASE + name, timeout=120) as response, temporary.open("wb") as output:
            total = int(response.headers.get("Content-Length", 0))
            downloaded = 0
            checkpoint = 0
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                output.write(chunk)
                downloaded += len(chunk)
                if downloaded - checkpoint >= 20 * 1024 * 1024:
                    print(f"  {downloaded // (1024*1024)} MB downloaded", flush=True)
                    checkpoint = downloaded
        if downloaded < 1_000_000 or (total and downloaded != total):
            raise RuntimeError("Incomplete voice download. Run Setup_Mood.bat again.")
        os.replace(temporary, target)
    prepare_runtime()
    subprocess.run([str(python), str(ROOT / "Check_Voice.py")], cwd=ROOT, check=True)

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("Setup error:", exc, flush=True)
        raise SystemExit(1)
