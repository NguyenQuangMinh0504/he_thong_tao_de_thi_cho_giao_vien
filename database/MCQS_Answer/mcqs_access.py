import pandas as pd

from database.path import QUESTION_PATH, MCQ_ANSWER_PATH

mcq_answer_table = pd.read_excel(MCQ_ANSWER_PATH)


def get_answer(question):
    question_table = pd.read_excel(QUESTION_PATH)
    merge_table = pd.merge(question_table, mcq_answer_table)
    query = "Question == '{}'".format(question)
    query_table = merge_table.query(query)
    return list(query_table["Dap_An"])


def delete_all_row(question_id):
    # currently has a bug
    question_table = pd.read_excel(QUESTION_PATH)
    merge_table = pd.merge(question_table, mcq_answer_table)
    query = "Question_ID == {}".format(question_id)
    query_table_index = merge_table.query(query).index
    mcq_answer_table.drop(query_table_index, inplace=True)


def insert_row(question_id, dap_an, true_false):
    mcq_answer_table.loc[-1] = [question_id, dap_an, true_false]
    mcq_answer_table.index += 1
    mcq_answer_table.sort_index(inplace=True)


def mcq_answer_table_save():
    mcq_answer_table.to_excel(MCQ_ANSWER_PATH, index=False)

