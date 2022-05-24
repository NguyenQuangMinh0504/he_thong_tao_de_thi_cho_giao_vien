import pandas as pd

from database.Question.question_access import get_feasible_question_on_difficulty, get_feasible_question_on_coverage
from database.Exam.exam_access import get_last_exam_id
from database.path import EXAM_QUESTION_PATH
exam_question_table = pd.read_csv(EXAM_QUESTION_PATH)


def insert_into_exam(exam_id, question_id, point):
    exam_question_table.loc[exam_question_table.shape[0]] = [exam_id, question_id, point]


def get_all_question(exam_id):
    query = "Exam_ID == {}".format(exam_id)
    return list(exam_question_table.query(query)["Question_ID"])


def save_exam_question_table():
    exam_question_table.to_csv(EXAM_QUESTION_PATH, index=False)


def get_exam_id(question_id):
    query = "Question_ID == {}".format(question_id)
    return list(exam_question_table.query(query)["Exam_ID"])


def auto_generate_exam_on_difficulty(subject_id, so_cau_de, so_cau_vua, so_cau_kho):
    for question_id in get_feasible_question_on_difficulty(subject_id, so_cau_de, so_cau_vua, so_cau_kho):
        insert_into_exam(get_last_exam_id(), question_id, 0)
    print(exam_question_table)


def auto_generate_exam_on_coverage(subject_id, coverage):
    for question_id in get_feasible_question_on_coverage(subject_id, coverage):
        insert_into_exam(get_last_exam_id(), question_id, 0)
    print(exam_question_table)


def remove_question_from_exam_question_table(question_id):
    query = "Question_ID == {}".format(question_id)
    exam_question_table.drop(exam_question_table.query(query).index, inplace=True)







