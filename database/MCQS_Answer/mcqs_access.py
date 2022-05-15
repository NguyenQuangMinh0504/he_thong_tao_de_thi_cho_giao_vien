import pandas as pd

from database.Question.question_access import question_table
from database.path import QUESTION_PATH, MCQ_ANSWER_PATH

mcq_answer_table = pd.read_csv(MCQ_ANSWER_PATH)


def get_answer(question_id):
    query = "Question_ID == {}".format(question_id)
    return list(mcq_answer_table.query(query)["Dap_An"])


def delete_all_row(question_id):
    query = "Question_ID == {}".format(question_id)
    mcq_answer_table.drop(mcq_answer_table.query(query).index, inplace=True)


def insert_row(question_id, dap_an, true_false):
    mcq_answer_table.loc[-1] = [question_id, dap_an, true_false]
    mcq_answer_table.index += 1
    mcq_answer_table.sort_index(inplace=True)


def get_right_answer(question_id):
    query = "Question_ID == {} and Correct_Answer == True".format(question_id)
    try:
        return list(mcq_answer_table.query(query)["Dap_An"])[0]
    except IndexError:
        print("No result")


def remove_answer(answer):
    query = "Dap_An == '{}'".format(answer)
    mcq_answer_table.drop(mcq_answer_table.query(query).index, inplace=True)


def save_mcq_answer_table():
    mcq_answer_table.to_csv(MCQ_ANSWER_PATH, index=False)


def load_mcq_answer_table():
    global mcq_answer_table
    mcq_answer_table = pd.read_excel(MCQ_ANSWER_PATH)

