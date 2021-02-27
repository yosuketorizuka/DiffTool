from module import readFileClass

filepath = r'DiffTool/import/'
filename = r'Trends_in_deaths1.csv'

if __name__ == '__main__':

    readfile_1 = readFileClass.readFileClass(filepath, filename)

    df = readfile_1.readFile()

    print(df)