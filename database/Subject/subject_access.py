import pandas as pd

from database.path import SUBJECT_PATH

subject_table = pd.read_csv(SUBJECT_PATH)


def get_all_subject():
    return list(subject_table["Subject_Name"])


def get_subject_info(subject_name):
    if subject_name == "":
        return False
    ma_hoc_phan = list(subject_table.loc[subject_table["Subject_Name"] == subject_name]["Course_Code"])[0]
    so_chuong = list(subject_table.loc[subject_table["Subject_Name"] == subject_name]["Num_Chapter"])[0]
    gioi_thieu = list(subject_table.loc[subject_table["Subject_Name"] == subject_name]["Description"])[0]
    return [ma_hoc_phan, so_chuong, gioi_thieu]


def get_subject_id(subject_name):
    query = "Subject_Name == \"{}\"".format(subject_name)
    if not subject_table.query(query).empty:
        return list(subject_table.query(query)["Subject_Id"])[0]
    return False


def get_subject_chapter(subject_id):
    query = "Subject_Id == {}".format(subject_id)
    if not subject_table.query(query).empty:
        return list(subject_table.query(query)["Num_Chapter"])[0]
    return False


def change_subject_info(subject_id, subject_name, course_code, num_chapter, description):
    query = "Subject_Id == {}".format(subject_id)
    subject_table.loc[subject_table.query(query).index] = [subject_id, subject_name, course_code, num_chapter, description]


def save_subject_table():
    subject_table.to_csv(SUBJECT_PATH, index=False)


def get_subject_name(subject_id):
    query = "Subject_Id == {}".format(subject_id)
    return list(subject_table.query(query)["Subject_Name"])[0]


def add_subject(subject_name, course_code, num_chapter, description):
    if subject_table.empty:
        last_question_id = 0
    else:
        last_question_id = subject_table.iloc[-1, 0]
    subject_table.loc[subject_table.shape[0]] = [last_question_id + 1, subject_name, course_code,
                                                 num_chapter, description]
    save_subject_table()


def remove_subject_from_subject_table(subject_id):
    from database.Question.question_access import get_info
    from database.Exam.exam_access import get_exam
    if len(get_info(subject_id)) == 0 and len(get_exam(subject_id)) == 0:
        query = "Subject_Id == {}".format(subject_id)
        subject_table.drop(subject_table.query(query).index, inplace=True)
        return True
    return False
