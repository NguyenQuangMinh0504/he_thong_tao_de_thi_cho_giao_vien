import pandas as pd

QUESTION_PATH = "../database/Question/Question.xlsx"

def get_answer(question):
    question_data = pd.read_excel(QUESTION_PATH)

    path = "../database/MCQS_Answer/MCQS_Answer.xlsx"
    mcqs_answer = pd.read_excel(path)

    merge_data = pd.merge(question_data, mcqs_answer)
    query = "Question == '{}'".format(question)
    filter_database = merge_data.query(query)
    return list(filter_database["Dap_An"])

