import glob
from pathlib import Path
import os

fls = os.listdir('../DS_10283_3038/DR-VCTK/DR-VCTK/clean_testset_wav_16k')

with open('test_vctk.txt', 'w') as f:
    for fl in fls:
        f.write('DS_10283_3038/DR-VCTK/DR-VCTK/clean_testset_wav_16k/' + fl + '\n')