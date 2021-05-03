import pandas as pd
import csv
from sklearn.model_selection import train_test_split


df_norm = pd.read_csv("D:\\Desktop\\Work\\Classifier - XSS\\normal-l.csv")
df_mal = pd.read_csv("D:\\Desktop\\Work\\Classifier - XSS\\malicious-l.csv")

df = pd.concat([df_norm, df_mal])

df = df.sample(frac=1).reset_index(drop=True)
#print(df)

train, test = train_test_split(df, test_size=0.2)
#print(train.reset_index(drop=True))
#print(test.reset_index(drop=True))

train.to_csv('train.csv')
test.to_csv('test.csv')
