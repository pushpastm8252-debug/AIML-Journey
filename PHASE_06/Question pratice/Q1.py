import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('train.txt',sep = ';',header = None,names = ['text','emotion'])
print(df.head())
print(df.isnull().sum())
unique_emotions = df['emotion'].unique()
emotion_numbers = {}
i = 0
for emo in unique_emotions:
  emotion_numbers[emo] = i
  i +=1

df['emotion'] = df['emotion'].map(emotion_numbers)
print(df)