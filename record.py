import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wav

def record(filename, duration = 5, fs = 22050):
    print(f"Register your voice")
    recording = sd.rec(int(duration *fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait(duration)
    wav.write(filename, fs, (recording * 32767).astype(np.int16))
    print(f"Saved {filename}")

if __name__ == "__main__":
    record("initial.wav", duration=5)