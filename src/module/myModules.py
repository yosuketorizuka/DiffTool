import pandas as pd

class readFileClass():

    df_out = pd.DataFrame()

    def setPara(self, filepath, filename):
        self.filepath = filepath
        self.filename = filename

    def readFile(self):

        # CSVファイルを読み込み
        df_out = pd.read_csv(self.filepath + self.filename)
        return df_out