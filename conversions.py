from CONSTANTS import colNamesMap, particOccupation, particEducation, particEducProgram, particVulnGroup
import numpy as np

def fixValueNames(dataframe):
    #replace Woman/Man
    mapping = {'V':'MAN', 'M':"WOMAN"}
    df = dataframe.replace({'gender':mapping})

    #replace the rest into categories
        #replace text to ints
    colsToReplace = df.columns[7:39]
    df[colsToReplace] = df[colsToReplace].notnull().astype('int')

    
    #df.fillna(0, inplace=True)
    df.fillna('', inplace=True)

    for c in colsToReplace:
        df[c] = df[c].astype("int64")
    #df["employerCode"] = df["employerCode"].astype("int64")

    #merge one-hot cols into categories
        #multiply by cat id
    colsToMult = df.columns[7:14]
    multiplyCols(df, colsToMult)
    df["occupation"] = df[colsToMult].sum(axis=1)
    df = df.replace({'occupation':particOccupation})

    colsToMult = df.columns[14:18]
    multiplyCols(df, colsToMult)
    df["education"] = df[colsToMult].sum(axis=1)
    df = df.replace({'education':particEducation})

    colsToMult = df.columns[18:20]
    multiplyCols(df, colsToMult)
    df["educProgram"] = df[colsToMult].sum(axis=1)
    df = df.replace({'educProgram':particEducProgram})

    df = df.drop(df.columns[7:20],axis = 1)

    print(df.head())
    return df

def renameCols(dataframe):
    dataframe.rename(columns=colNamesMap,inplace = True)


def multiplyCols(df, colsToMult):
    count = len(colsToMult)
    for i in range(0, count):
        df[colsToMult[i]] = df[colsToMult[i]]*(i+1)