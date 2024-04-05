import librosa
import soundfile as sf
from pathlib import Path
import glob

def resample(path, target_sr=16000, output_path=None):
    y, sr = sf.read(path)
    y = librosa.resample(y, orig_sr=22050, target_sr=target_sr)
    if output_path:
        sf.write(output_path, y, target_sr)
    else:
        sf.write(path, y, target_sr)

for item in Path('finetune/wavs').glob("*.wav"):
    resample(item)