import numpy as np
import pandas as pd
import argparse
from pathlib import Path

def rolling(df,args,intfrompath,filepath):
    df2 = df.copy(deep=True)
    # creating a copy of dataframe in case it's needed later
    rowsize = intfrompath
    dfempty = pd.DataFrame(np.nan, index=np.arange(rowsize), columns=df2.columns)
    #empty dataframe with column labels same as original, number of rows equal to arg pass, filled empty
    if args.top == True:
        df2 = pd.concat([dfempty,df2], ignore_index=True, axis=0)
    else:
        df2 = pd.concat([df2,dfempty], ignore_index=True, axis=0)
    #merging
    df2.to_csv(filepath, index=False)

def main():
    parser = argparse.ArgumentParser(
                    prog='Drumroll',
                    description='Adds empty rows at the top of csv files',
                    epilog='Bottom text')
    parser.add_argument('filepath', type=Path)
    parser.add_argument('integer', type=int)
    parser.add_argument('-t', '--top', action='store_true')

    args = parser.parse_args()
    intfrompath = args.integer
    extentiontype = '.csv'
    filepath = args.filepath.stem + extentiontype
#sanitizes input to allow declaration of file without extension

    df = pd.read_csv(filepath)
    rolling(df,args,intfrompath,filepath)

if __name__ == "__main__":
    main()