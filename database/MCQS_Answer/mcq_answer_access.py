import pandas as pd

from database.path import QUESTION_PATH, MCQ_ANSWER_PATH

mcq_answer_table = pd.read_csv(MCQ_ANSWER_PATH)


def get_all_answer(question_id):
    query = "Question_ID == {}".format(question_id)
    return list(mcq_answer_table.query(query)["Dap_An"])


def get_all_correct_answer(question_id):
    query = "Question_ID == {} and Correct_Answer == True".format(question_id)
    return list(mcq_answer_table.query(query)["Dap_An"])


def remove_question_and_answer_from_mcq_answer_table(question_id):
    query = "Question_ID == {}".format(question_id)
    mcq_answer_table.drop(mcq_answer_table.query(query).index, inplace=True)


def insert_row(question_id, dap_an, true_false):
    mcq_answer_table.loc[mcq_answer_table.shape[0]] = [question_id, dap_an, true_false]



    try:
        return list(mcq_answer_table.query(query)["Dap_An"])[0]
    except IndexError:
        print("No result")


def remove_answer(answer):
    query = "Dap_An == \"{}\"".format(answer)
    mcq_answer_table.drop(mcq_answer_table.query(query).index, inplace=True)


def modify_correct(answer, correct):
    query = "Dap_An == \"{}\"".format(answer)
    mcq_answer_table.loc[mcq_answer_table.query(query).index[0], "Correct_Answer"] = correct


def get_answer_correct(answer):
    query = "Dap_An == \"{}\"".format(answer)
    print(list(mcq_answer_table.query(query)["Correct_Answer"]))
    return list(mcq_answer_table.query(query)["Correct_Answer"])[0]


def save_mcq_answer_table():
    mcq_answer_table.to_csv(MCQ_ANSWER_PATH, index=False)

