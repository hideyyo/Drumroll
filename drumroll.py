import numpy as np
import pandas as pd
import argparse
from pathlib import Path

def rolling(df):
    df2 = df.copy(deep=True)
    # creating a copy of dataframe in case it's needed later
    rowsize = intfrompath
    dfempty = pd.DataFrame(np.nan, index=np.arange(rowsize), columns=df2.columns)
    #empty dataframe with column labels same as original, number of rows equal to arg pass, filled empty
    df2 = pd.concat([df2,dfempty], ignore_index=True, axis=0)
    #merging
    df2 = df2.iloc[::-1]
    #reversing the dataframe
    df2.to_csv('testoutput.csv', index=False)

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
#sanitizes input to allow declaration of file without extention

df = pd.read_csv(filepath)
rolling(df)