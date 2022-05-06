import os

import pandas as pd


def get_subject_name():
    path = "./Subject/Subject.xlsx"
    abs_path = os.path.abspath(path)
    print(abs_path)
    subject = pd.read_excel(io=abs_path)
    print(subject)
    return list(subject["Tên môn học"])

if __name__ == '__main__':
    get_subject_name()
