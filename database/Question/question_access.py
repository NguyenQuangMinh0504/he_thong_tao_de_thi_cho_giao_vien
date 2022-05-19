import pandas as pd

from database.path import QUESTION_PATH


question_table = pd.read_csv(QUESTION_PATH)


def get_info():
    return list(question_table["Question"])


def get_trac_nghiem_info(subject_id):
    query = "Type == \"trac_nghiem\" and Subject_ID == {}".format(subject_id)
    filter_database = question_table.query(query)
    return list(filter_database["Question"])


def get_tu_luan_info(subject_id):
    query = "Type == \"tu_luan\" and  Subject_ID == {}".format(subject_id)
    filter_database = question_table.query(query)
    return list(filter_database["Question"])


def get_question_difficulty(question_id):
    query = "Question_ID == {}".format(question_id)
    return str(list(question_table.query(query)["Difficulty"])[0])


def get_question_chapter(question_id):
    query = "Question_ID == {}".format(question_id)
    return str(list(question_table.query(query)["Chapter"])[0])


def get_question_id(question):
    query = "Question == \"{}\"".format(question)
    query_data = list(question_table.query(query)["Question_ID"])
    if not query_data:
        print("there is no matching row")
    else:
        return str(list(question_table.query(query)["Question_ID"])[0])


def delete_question_from_question_table(question_id):
    query = "Question_ID == {}".format(question_id)
    question_table.drop(question_table.query(query).index, inplace=True)


def add_question(question, subject_id, question_type, difficulty, chapter):
    last_question_id = question_table.iloc[-1, 0]
    question_table.loc[-1] = [last_question_id + 1, question, subject_id, question_type, difficulty, chapter]
    question_table.index += 1
    question_table.sort_index(inplace=True)


def save_question_table():
    question_table.to_csv(index=False)



