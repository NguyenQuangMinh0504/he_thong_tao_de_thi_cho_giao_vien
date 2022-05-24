import pandas as pd
from database.path import EXAM_PATH
exam_table = pd.read_csv(EXAM_PATH)


def get_all_description():
    print(list(exam_table["Exam_ID"]))


def insert_to_exam(subject_id, description, school_year, duration, semester):
    last_exam_id = exam_table.iloc[-1, 0]
    exam_table.loc[exam_table.shape[0]] = [last_exam_id + 1, subject_id, description, school_year, duration, semester]


def get_last_exam_id():
    return exam_table.iloc[-1, 0] + 1


def save_exam_table():
    exam_table.to_csv(EXAM_PATH, index=False)


def get_exam(subject_id):
    query = "Subject_ID == {}".format(subject_id)
    filter_table = exam_table.query(query)
    exam_info = []
    for i in filter_table.index:
        exam_info.append(list(filter_table.loc[i]))
    return exam_info


def get_exam_info(exam_id):
    query = "Exam_ID == {}".format(exam_id)
    filter_table = exam_table.query(query)
    if len(filter_table) != 0:
        return list(filter_table.loc[filter_table.index[0]])
    return False


def get_exam_info_string(exam_id):
    query = "Exam_ID == {}".format(exam_id)
    info = list(exam_table.loc[exam_table.query(query).index[0]])
    return "{} năm học {} kỳ {}".format(info[2], info[3], info[5])





