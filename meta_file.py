import pandas as pd
import numpy as np

test_file = 'consumptive_snippets.csv'
df = pd.read_csv(test_file, low_memory=False)

df = df.dropna()
df = df.drop('Unnamed: 0', axis=1)

print(df)
print(df.columns)
print(df['File Name'])

df.to_csv('clean_consumptive_snippets.csv')
