import os
import __main__ as main
from os import path
import re 
import pandas as pd


def ReadXLSX(filePath):
    part1 = pd.read_excel(filePath, header=[14], comment='*', dtype=str)#converters={'PDD5': str, 'DD2' : str})
    cols_to_drop = part1.columns[44:]
    part1 = part1.drop(cols_to_drop, axis=1)
    part1.dropna(how='all',axis=0, inplace=True)
    return part1

def ReadResultXLSX(filePath):
    part1 = pd.read_excel(filePath, header=[0], comment='*', dtype=str)#converters={'PDD5': str, 'DD2' : str})
    #cols_to_drop = part1.columns[44:]
    #part1 = part1.drop(cols_to_drop, axis=1)
    part1.dropna(how='all',axis=0, inplace=True)
    return part1

def getInputFilePaths():
    curr_path = path.dirname(path.abspath(main.__file__))
    abs_path = path.join(curr_path, "IO")
    outputPaths = []
    for root, dirs, files in os.walk(abs_path):
        for file in files:
            if file.endswith(".xlsx"):
                outputPaths.append(os.path.join(root, file))
    return outputPaths

def ReadFiles():
    paths = getInputFilePaths()
    dfList = []
    for p in paths:
        print(p)
        dfList.append(ReadXLSX(p))
    if len(dfList) ==0:
        return None
    df = pd.concat(dfList, axis=0, ignore_index=False)
    return df

def ReadResultFiles():
    paths = getInputFilePaths()
    dfList = []
    for p in paths:
        print(p)
        dfList.append(ReadResultXLSX(p))
    if len(dfList) ==0:
        return None
    df = pd.concat(dfList, axis=0, ignore_index=False)
    return df

def TryMakeIO():
    curr_path = path.dirname(path.abspath(main.__file__))
    abs_path = path.join(curr_path, "IO")
    try:
        os.mkdir(abs_path)
    except:
        pass