import pandas as pd


def export_to_json_file(dataframe: pd.DataFrame, fp:str):
    if fp == "":
        print("File path not exist !")
    else:
        dataframe.to_json(fp)


def import_json_file(fp: str):
    if fp == "":
        print("File path not exist !")
    else:
        table = pd.read_json(fp)
        print(table)
        pass


if __name__ == '__main__':
    test = pd.read_csv("../database/Question/Question.csv")
    print(test)
    a = test.to_json()
    print(a)

