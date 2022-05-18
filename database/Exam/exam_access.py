import pandas as pd
from database.path import EXAM_PATH
exam = pd.read_csv(EXAM_PATH)


def get_all_description():
    print(list(exam["Exam_ID"]))


def insert_to_exam():
    print("foo")
    last_id = exam.iloc[-1, 0]


