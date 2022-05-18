import pandas as pd

from database.path import SUBJECT_PATH

subject = pd.read_csv(SUBJECT_PATH)


def get_subject_name():
    return list(subject["Tên môn học"])


def get_subject_info(name):
    ma_hoc_phan = list(subject.loc[subject["Tên môn học"] == name]["Mã học phần"])[0]
    so_chuong = list(subject.loc[subject["Tên môn học"] == name]["Số chương"])[0]
    gioi_thieu = list(subject.loc[subject["Tên môn học"] == name]["Giới thiệu"])[0]
    return [ma_hoc_phan, so_chuong, gioi_thieu]



