class readFileClass():

#    def __init__(self, filepath, filename):
#        self.filepath = filepath
#        self.filename = filename

    def setParameter(self, filepath, filename):
        self.filepath = filepath
        self.filename = filename

    def readFile(self):

        import pandas as pd

        # CSVファイルを読み込み
        df = pd.read_csv(self.filepath + self.filename)

        return df