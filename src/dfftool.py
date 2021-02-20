import pandas as pd

importFilePath = r'DiffTool/import/'
importFileName1 = r'Trends_in_deaths1.csv'
importFileName2 = r'Trends_in_deaths2.csv'
exportFilePath = r'DiffTool/export/'
exportFileName = r'data_result.csv'

def readFile():

    # import用のDataframeを宣言
    global df_deathRate1
    global df_deathRate2
    global df_deathRate1_sorted
    global df_deathRate2_sorted
    global df_deathRate1_sorted_r
    global df_deathRate2_sorted_r

    # CSVファイルを読み込み
    df_deathRate1 = pd.read_csv(importFilePath + importFileName1)
    df_deathRate2 = pd.read_csv(importFilePath + importFileName2)

    # ソート
    df_deathRate1_sorted = df_deathRate1.sort_values('Year')
    df_deathRate2_sorted = df_deathRate2.sort_values('Year')

    #indexふり直し
    #df_r = df.reset_index()
    df_deathRate1_sorted_r = df_deathRate1_sorted.reset_index()
    df_deathRate2_sorted_r = df_deathRate2_sorted.reset_index()

    print("read file completed")

def get_column():

    num_columns = len(df_deathRate1.columns)

    global l_columns
    l_columns = []

    for i in range(num_columns):
        l_columns.append(df_deathRate1.columns.values[i])

    print("get_colume completed")


def check_diff():

    global df_deathRate_output
    # Input用のDataframeを空で複製
    df_deathRate_output = pd.DataFrame().reindex_like(df_deathRate1)
    # Output用のDataFrameを初期化
    df_deathRate_output.drop(df_deathRate_output.index, inplace=True)

    for wk_col in l_columns:
        for idx, seri in df_deathRate1_sorted_r.iterrows():
            if seri[wk_col] == df_deathRate2_sorted_r.loc[idx, wk_col]:
                continue
            else:
                df_deathRate_output = df_deathRate_output.append(seri)
                df_deathRate_output = df_deathRate_output.append(df_deathRate2_sorted_r.loc[idx])

    print("check_diff completed")

def output():
    df_deathRate_output.to_csv(exportFilePath + exportFileName, index=False)
    print("output completed")

if __name__ == "__main__":

    readFile()

    get_column()

    check_diff()

    output()