import pandas as pd


def get_subject_name():
    path = "../database/Subject/Subject.xlsx"
    subject = pd.read_excel(path)
    return list(subject["Tên môn học"])


def get_subject_info(name):
    path = "../database/Subject/Subject.xlsx"
    subject = pd.read_excel(path)
    ma_hoc_phan = list(subject.loc[subject["Tên môn học"] == name]["Mã học phần"])[0]
    so_chuong = list(subject.loc[subject["Tên môn học"] == name]["Số chương"])[0]
    gioi_thieu = list(subject.loc[subject["Tên môn học"] == name]["Giới thiệu"])[0]
    return [ma_hoc_phan, so_chuong, gioi_thieu]


if __name__ == '__main__':
    get_subject_info("Tương tác người máy")


