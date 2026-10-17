"""Build the complete shareable Mood folder on Windows."""
from pathlib import Path
import shutil
import subprocess
import sys
from setup_mood import prepare_runtime

ROOT = Path(__file__).resolve().parent

def main():
    if sys.platform != 'win32':
        raise RuntimeError('Build Mood on Windows.')
    prepare_runtime()
    subprocess.run([sys.executable, str(ROOT / 'Check_Voice.py')], cwd=ROOT, check=True)
    command = [sys.executable, '-m', 'PyInstaller', '--noconfirm', '--clean',
               '--onedir', '--windowed', '--name', 'Mood', '--icon', str(ROOT / 'Mood.ico')]
    for module in ('webview', 'kokoro_onnx', 'espeakng_loader', 'phonemizer',
                   'onnxruntime', 'sounddevice', '_sounddevice_data'):
        command += ['--collect-all', module]
    command += ['--copy-metadata', 'phonemizer', '--copy-metadata', 'kokoro-onnx',
                '--add-data', str(ROOT / 'voices') + ':voices', str(ROOT / 'techaid_io.py')]
    subprocess.run(command, cwd=ROOT, check=True)
    destination = ROOT / 'dist' / 'Mood'
    shutil.copytree(ROOT / 'runtime', destination / 'runtime', dirs_exist_ok=True)
    (destination / 'START-HERE.txt').write_text(
        'Welcome to Mood!\n\nOpen Mood.exe. Keep all these files together.\n'
        'First launch downloads llama2-uncensored automatically (several GB).\n'
        'Stay connected to the internet and keep Mood open until it says ready.\n'
        'If a connection fails, click Retry setup.\n'
        'After setup, chat and Kokoro Heart speech run locally.\n'
        'No Python or separate Ollama installation is needed.\n', encoding='utf-8')
    print('READY TO SHARE:', destination, flush=True)
    print('Zip the entire Mood folder inside dist and send it to friends.', flush=True)

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('Build error:', exc, flush=True)
        raise SystemExit(1)
