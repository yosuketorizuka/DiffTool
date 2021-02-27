import pandas as pd
from module import myModules

importFilePath = r'DiffTool/import/'
importFileName1 = r'Trends_in_deaths1.csv'
importFileName2 = r'Trends_in_deaths2.csv'
exportFilePath = r'DiffTool/export/'
exportFileName = r'data_result.csv'

#df_in_1 = pd.DataFrame()
#df_in_2 = pd.DataFrame()
#df_out = pd.DataFrame()

dfCol = []
numCol = 0

def getData():

    global df_in_1
    global df_in_2

    readFile_1 = myModules.readFileClass()
    readFile_1.setPara(importFilePath, importFileName1)
    df_in_1 = readFile_1.readFile()

    readFile_2 = myModules.readFileClass()
    readFile_2.setPara(importFilePath, importFileName2)
    df_in_2 = readFile_2.readFile()

def getCol():

    global numCol
    global dfCol

    numCol = len(df_in_1.columns)

    for i in range(numCol):
        dfCol.append(df_in_1.columns.values[i])

def difFile():

    global df_out
    df_out = pd.DataFrame()

    df_out = pd.DataFrame().reindex_like(df_in_1)
    # Output用のDataFrameを初期化
    df_out.drop(df_out.index, inplace=True)

    for wk_col in dfCol:
        for idx, seri in df_in_1.iterrows():
            if seri[wk_col] == df_in_2.loc[idx, wk_col]:
                continue
            else:
                df_out = df_out.append(seri)
                df_out = df_out.append(df_in_2.loc[idx])


def outData():

    writeFile = myModules.writeFileClass()
    writeFile.setPara(exportFilePath, exportFileName, df_out)
    writeFile.writeFile()

if __name__ == "__main__":

    getData()

    getCol()

    difFile()

    outData()

    print('all process completed')
