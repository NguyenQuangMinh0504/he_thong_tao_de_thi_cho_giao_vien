import pandas as pd

from database.path import QUESTION_PATH


question_table = pd.read_csv(QUESTION_PATH)


def get_info(subject_id):
    query = "Subject_ID == {}".format(subject_id)
    filter_table = question_table.query(query)
    return list(filter_table["Question"])


def get_trac_nghiem_info(subject_id):
    query = "Type == \"trac_nghiem\" and Subject_ID == {}".format(subject_id)
    filter_table = question_table.query(query)
    return list(filter_table["Question"])


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
    question_table.loc[question_table.shape[0]] = [last_question_id + 1, question, subject_id,
                                                   question_type, difficulty, chapter]


def save_question_table():
    question_table.to_csv(QUESTION_PATH, index=False)


def get_question(question_id):
    query = "Question_ID == {}".format(question_id)
    return str(list(question_table.query(query)["Question"])[0])


def get_feasible_question_on_difficulty(subject_id, so_cau_de, so_cau_vua, so_cau_kho):
    query1 = "Subject_ID == {} and Difficulty == 1".format(subject_id)
    query2 = "Subject_ID == {} and Difficulty == 2".format(subject_id)
    query3 = "Subject_ID == {} and Difficulty == 3".format(subject_id)
    so_cau_de_index = list(question_table.query(query1).index)
    so_cau_vua_index = list(question_table.query(query2).index)
    so_cau_kho_index = list(question_table.query(query3).index)
    if len(so_cau_de_index) < so_cau_de:
        return False
    elif len(so_cau_vua_index) < so_cau_vua:
        return False
    elif len(so_cau_kho_index) < so_cau_kho:
        return False
    indexes = so_cau_de_index[:so_cau_de] + so_cau_vua_index[:so_cau_vua] + so_cau_kho_index[:so_cau_kho]
    question_ids = []
    for index in indexes:
        question_ids.append(question_table.loc[index]["Question_ID"])
    return question_ids


def get_feasible_question_on_coverage(subject_id, coverage):
    indexes = []
    for i, j in enumerate(coverage):
        query = "Subject_ID == {} and Chapter == {}".format(subject_id, i+1)
        chapter_index = list(question_table.query(query).index)
        if len(chapter_index) < j:
            return False
        indexes += chapter_index[:j]
    question_ids = []
    for index in indexes:
        question_ids.append(question_table.loc[index]["Question_ID"])
    return question_ids















