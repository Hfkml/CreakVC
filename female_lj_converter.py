from pathlib import Path
from glob import glob
import os

levels = [0.0, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8]
# levels = [1, 0.8, 0.6, 1.2]
for item in Path('./audio/joe_interspeech').glob('*.wav'):
    for level in levels:
        os.system(f"python run.py {item} audio//enhanced_creak/male_high_creak_extra.wav audio/enhanced_creak/male_no_creak.wav {level} outputs/joe_interspeech/{level}/{item.stem}_20000.wav")