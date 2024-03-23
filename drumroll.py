import numpy as np
import pandas as pd
import argparse
from pathlib import Path

def rolling(df):
    df2 = df.copy(deep=True)
    s1 = intfrompath
    s2 = len(df2.columns)
    print(f's1 is {s1} and s2 is {s2}')
    arrhere = pd.DataFrame((np.empty((s2,s1))), columns=df.columns)
    df2 = pd.concat([df2,arrhere], ignore_index=True)
    df2 = df2.iloc[::-1]
    df2.to_csv('testoutput.csv', index=False)
    df2.head()

parser = argparse.ArgumentParser(
                    prog='Drumroll',
                    description='Adds empty rows at the top of csv files',
                    epilog='Bottom text')
parser.add_argument('filepath', type=Path)
parser.add_argument('integer', type=int)

args = parser.parse_args()
intfrompath = args.integer
extentiontype = '.csv'
filepath = args.filepath.stem + extentiontype

df = pd.read_csv(filepath)
df.head()
rolling(df)