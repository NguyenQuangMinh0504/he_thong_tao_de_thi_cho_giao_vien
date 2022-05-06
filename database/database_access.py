import pandas as pd


def get_subject_name():
    path = "../database/Subject/Subject.xlsx"
    subject = pd.read_excel(path)
    return list(subject["Tên môn học"])
