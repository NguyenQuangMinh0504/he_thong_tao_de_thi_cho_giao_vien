import pandas
import json


def export_to_json(dataframe: pandas.DataFrame, fp: str):
    value = dataframe.values.tolist()
    if fp == "":
        print("File path not exist !")
    else:
        with open(fp, "w") as outfile:
            json.dump(value, outfile)
