from module import myModules

filepath_in = r'DiffTool/import/'
filename_in = r'Trends_in_deaths1.csv'
filepath_out = r'DiffTool/export/'
filename_out = r'Trends_out_deaths1.csv'


if __name__ == '__main__':

    readfile_1 = myModules.readFileClass()
    readfile_1.setPara(filepath_in, filename_in)
    df = readfile_1.readFile()
    

    wrirefile_1 = myModules.wrireFileClass()
    wrirefile_1.setPara(filepath_out, filename_out, df)
    wrirefile_1.writeFile()