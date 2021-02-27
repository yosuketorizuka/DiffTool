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

    def writeFile(self):
        self.df_out.to_csv(self.filepath + self.filename, index=False)