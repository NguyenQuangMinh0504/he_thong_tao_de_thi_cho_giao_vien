import pandas as pd
from database.path import EXAM_PATH
exam = pd.read_csv("./Exam.csv")
print(exam)


def get_all_description():
    print(list(exam["Exam_ID"]))


get_all_description()


