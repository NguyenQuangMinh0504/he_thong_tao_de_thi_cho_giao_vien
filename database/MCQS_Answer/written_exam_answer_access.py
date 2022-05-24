import pandas as pd
from database.path import WRITTEN_EXAM_ANSWER_PATH

written_exam_answer_table = pd.read_csv(WRITTEN_EXAM_ANSWER_PATH)


def insert_answer_or_modify_current_answer_to_written_exam_answer_table(question_id, answer):
    query = "Question_ID == {}".format(question_id)
    index = written_exam_answer_table.query(query).index
    if len(index) == 0:
        written_exam_answer_table.loc[written_exam_answer_table.shape[0]] = [question_id, answer]
    else:
        written_exam_answer_table.loc[written_exam_answer_table.query(query).index[0], "Answer"] = answer


def get_written_answer(question_id):
    query = "Question_ID == {}".format(question_id)
    if len(written_exam_answer_table.query(query).index) == 0:
        return False
    else:
        return written_exam_answer_table.loc[written_exam_answer_table.query(query).index[0], "Answer"]


def save_written_exam_answer_table():
    written_exam_answer_table.to_csv(WRITTEN_EXAM_ANSWER_PATH, index=False)


def remove_question_and_answer_from_written_exam_answer_table(question_id):
    query = "Question_ID == {}".format(question_id)
    written_exam_answer_table.drop(written_exam_answer_table.query(query).index, inplace=True)
    print(written_exam_answer_table)

