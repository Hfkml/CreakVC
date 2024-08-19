from pathlib import Path
from glob import glob
import numpy as np
import pandas as pd
import soundfile as sf 

df = pd.read_csv('./combined_cpps.csv', sep='\t')
win_len = 1280
hop_len = 320

#add column headers
df.columns = ['FileName', 'CPPvoiceDet']

df['FileName'] = df['FileName'].apply(lambda x: '/nfs/deepspeech/home/lameris/libri_train/test/wavs/' + x)
df['CPPvoiceDet'] = df['CPPvoiceDet'].apply(lambda x: float(x)) 
#ind mean and std of the CPPvoiceDet values
mean = df['CPPvoiceDet'].mean()
std = df['CPPvoiceDet'].std()
print('mean', mean, 'std', std)

#mean 12.281818111279561 std 1.6241459175290687
for i, row in df.iterrows():
    #get num of samples
    #wav, sr = sf.read('/nfs/deepspeech/home/lameris/' + '/'.join(row['FileName'].split('/')[-3:]))
    try:
        wav, sr = sf.read(row['FileName'])
    except:
        print('Error: ' + row['FileName'])
        continue
    
    windows = (len(wav) - win_len) // hop_len + 5
    #use data at CPPvoiceDet in this row and create an np array of (1, windows) of the value
    data = np.zeros((windows)) + (float(row['CPPvoiceDet']) - 12.281818111279561) / 1.6241459175290687
    np.save(row['FileName'].replace('wavs', 'cpps').replace('.wav', '.npy'), data)




