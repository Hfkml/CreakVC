import glob
from pathlib import Path
import os

fls = os.listdir('../finetune/train/wavs')

with open('train_vctk.txt', 'w') as f:
    for fl in fls:
        f.write(f"./finetune/train/wavs/{fl}\n")