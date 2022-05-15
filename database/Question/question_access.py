import pandas as pd

from database.path import QUESTION_PATH


question_table = pd.read_csv(QUESTION_PATH)


def get_info():
    return list(question_table["Question"])


def get_trac_nghiem_info():
    query = "Type == 'trac_nghiem'"
    filter_database = question_table.query(query)
    return list(filter_database["Question"])


def get_tu_luan_info():
    query = "Type == 'tu_luan'"
    filter_database = question_table.query(query)
    return list(filter_database["Question"])


def get_question_difficulty(question_id):
    query = "Question_ID == {}".format(question_id)
    return str(list(question_table.query(query)["Difficulty"])[0])


def get_question_chapter(question_id):
    query = "Question_ID == {}".format(question_id)
    return str(list(question_table.query(query)["Chapter"])[0])


def get_question_id(question):
    query = "Question == '{}'".format(question)
    return str(list(question_table.query(query)["Question_ID"])[0])


def delete_question_from_question_table(question_id):
    query = "Question_ID == {}".format(question_id)
    question_table.drop(question_table.query(query).index, inplace=True)

# def add_question(question):


def save_question_table():
    question_table.to_csv(index=False)





