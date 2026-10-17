"""Check the real model and save a playable sample before building an exe."""
from pathlib import Path
import wave
import numpy as np
from kokoro_onnx import Kokoro
from techaid_io import KokoroVoice

folder = KokoroVoice.model_directory()
print("Checking Kokoro Heart. Initial model loading may take a moment...", flush=True)
engine = Kokoro(str(folder / "kokoro-v1.0.onnx"), str(folder / "voices-v1.0.bin"))
audio, rate = engine.create("Hi, I'm Mood. What would you like to work on today?", voice="af_heart", speed=1.0, lang="en-us")
if rate <= 0 or len(audio) == 0:
    raise RuntimeError("The voice returned no audio.")
path = Path(__file__).resolve().parent / "Mood-voice-test.wav"
with wave.open(str(path), "wb") as output:
    output.setnchannels(1)
    output.setsampwidth(2)
    output.setframerate(rate)
    output.writeframes((np.clip(audio, -1, 1) * 32767).astype("<i2").tobytes())
print("Voice model works. Sample saved:", path, flush=True)
