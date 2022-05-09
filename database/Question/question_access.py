import pandas as pd


def get_trac_nghiem_info():
    path = "../database/Question/Question.xlsx"
    question_data = pd.read_excel(path)
    query = "Type == 'trac_nghiem'"
    filter_database = question_data.query(query)
    return list(filter_database["Question"])

def get_tu_luan_info():
    path = "../database/Question/Question.xlsx"
    question_data = pd.read_excel(path)
    query = "Type == 'tu_luan'"
    filter_database = question_data.query(query)
    return list(filter_database["Question"])
