import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('train.txt',sep = ';',header = None,names = ['text','emotion'])
     

df.head()    
df.isnull().sum()