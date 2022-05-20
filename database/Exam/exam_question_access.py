import pandas as pd
from database.path import EXAM_QUESTION_PATH
exam_question_table = pd.read_csv(EXAM_QUESTION_PATH)


def insert_into_exam(exam_id, question_id, point):
    exam_question_table.loc[-1] = [exam_id, question_id, point]
    exam_question_table.index += 1
    exam_question_table.sort_index(inplace=True)
    print(exam_question_table)


def get_all_question(exam_id):
    query = "Exam_ID == {}".format(exam_id)
    return list(exam_question_table.query(query)["Question_ID"])


def save_exam_question_table():
    exam_question_table.to_csv(EXAM_QUESTION_PATH, index=False)
