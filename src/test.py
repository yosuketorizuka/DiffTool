from module import myModules

filepath = r'DiffTool/import/'
filename = r'Trends_in_deaths1.csv'

if __name__ == '__main__':

    readfile_1 = myModules.readFileClass()

    readfile_1.setPara(filepath, filename)

    df = readfile_1.readFile()
    
    print(df)