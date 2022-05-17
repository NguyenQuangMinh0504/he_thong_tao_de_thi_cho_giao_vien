import pandas as pd
from database.path import EXAM_PATH
exam = pd.read_csv(EXAM_PATH)


def get_all_description():
    print(exam["Exam_ID"])
    return list(exam["Exam_ID"])


