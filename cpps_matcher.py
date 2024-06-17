from pathlib import Path
from glob import glob
import numpy as np
import pandas as pd
import soundfile as sf 

df = pd.read_csv('./cpps_train.txt', sep='\t')
win_len = 1280
hop_len = 320

df['FileName'] = df['FileName'].apply(lambda x: './finetune/train/wavs/' + x + '.wav')

#find mean and std of the CPPvoiceDet values
#mean = df['CPPvoiceDet'].mean()
#std = df['CPPvoiceDet'].std()


for i, row in df.iterrows():
    #get num of samples
    wav, sr = sf.read(row['FileName'])
    windows = (len(wav) - win_len) // hop_len + 5
    #use data at CPPvoiceDet in this row and create an np array of (1, windows) of the value
    data = np.zeros((windows)) + (float(row['CPPvoiceDet']) - 11.348930184008122) / 1.6515730095764132
    #save the data
    np.save(row['FileName'].replace('wavs', 'cpps').replace('.wav', '.npy'), data)




