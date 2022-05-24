import pandas as pd
from database.path import WRITTEN_EXAM_ANSWER_PATH

written_exam_answer_table = pd.read_csv(WRITTEN_EXAM_ANSWER_PATH)


def modify_answer(question_id, answer):
    query = "Question_ID == {}".format(question_id)
    written_exam_answer_table.loc[written_exam_answer_table.query(query).index[0], "Answer"] = answer


def insert_answer(question_id, answer):
    written_exam_answer_table.loc[written_exam_answer_table.shape[0]] = [question_id, answer]
    print(written_exam_answer_table)


def save_written_exam_answer_table():
    written_exam_answer_table.to_csv(WRITTEN_EXAM_ANSWER_PATH, index=False)





