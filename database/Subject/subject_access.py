import pandas as pd

from database.path import SUBJECT_PATH

subject_table = pd.read_csv(SUBJECT_PATH)


def get_subject_name():
    return list(subject_table["Subject_Name"])


def get_subject_info(subject_name):
    ma_hoc_phan = list(subject_table.loc[subject_table["Subject_Name"] == subject_name]["Mã học phần"])[0]
    so_chuong = list(subject_table.loc[subject_table["Subject_Name"] == subject_name]["Num_Chapter"])[0]
    gioi_thieu = list(subject_table.loc[subject_table["Subject_Name"] == subject_name]["Giới thiệu"])[0]
    return [ma_hoc_phan, so_chuong, gioi_thieu]


def get_subject_id(subject_name):
    query = "Subject_Name == \"{}\"".format(subject_name)
    return str(list(subject_table.query(query)["Subject_Id"])[0])


def get_subject_chapter(subject_id):
    query = "Subject_Id == {}".format(subject_id)
    return int(list(subject_table.query(query)["Num_Chapter"])[0])


