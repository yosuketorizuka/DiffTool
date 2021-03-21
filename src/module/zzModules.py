import pandas as pd

class readFileClass():

    df_in = pd.DataFrame()

    def setPara(self, filepath, filename):
        self.filepath = filepath
        self.filename = filename

    def readFile(self):

        # CSVファイルを読み込み
        df_in = pd.read_csv(self.filepath + self.filename)
        return df_in

class writeFileClass():

    df_out = pd.DataFrame()

    def setPara(self, filepath, filename, df_out):
        self.filepath = filepath
        self.filename = filename
        self.df_out = df_out

    # CSVファイルへ書き出し
    def writeFile(self):
        self.df_out.to_csv(self.filepath + self.filename, index=False)

class getColClass():

    df_in = pd.DataFrame()
    dfCol = []

    def setPara(self, df_in):
        self.df_in = df_in

    def getCol(self):
        
        numCol = len(self.df_in.columns)

        for i in range(numCol):
            self.dfCol.append(self.df_in.columns.values[i])

        return self.dfCol