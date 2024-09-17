import librosa
import soundfile as sf
from pathlib import Path
import glob

def resample(path, target_sr=16000, output_path=None):
    y, sr = sf.read(path)
    y = librosa.resample(y, orig_sr=48000, target_sr=target_sr)
    if output_path:
        sf.write(output_path, y, target_sr)
    else:
        sf.write(path, y, target_sr)

resample('test_audio/joe_example.wav', target_sr=16000, output_path='test_audio/16000_joe_example_compare.wav')
