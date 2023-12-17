# load file
file_path = 'dataset_full.txt'
# read file
with open(file_path,'r') as f:
  df=f.readlines()
import pandas as pd
df=pd.read_csv(file_path, sep='\t', engine='python', encoding='cp949')

# split train/test/val files
import numpy as np

train, validate, test = np.split(df.sample(frac=1), [int(.6*len(df)), int(.8*len(df))])

# save files                                                                                                                                                                                                         
train.to_csv('train_files.txt', sep='\n', index=False)
validate.to_csv('val_files.txt', sep='\n', index=False)
test.to_csv('test_files.txt', sep='\n', index=False)
