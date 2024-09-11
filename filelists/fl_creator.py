from glob import glob
from pathlib import Path
import os

fls = glob('/nfs/deepspeech/home/lameris/libri_train/test/wavs/*.wav')

with open('test_libri.txt', 'w') as f:
    for fl in fls:
        f.write(f"/nfs/deepspeech/home/lameris/libri_train/test/wavs/{Path(fl).stem}.wav\n")