import pandas as pd

from database.path import QUESTION_PATH


question_table = pd.read_csv(QUESTION_PATH)


def get_info(subject_id):

    query = "Subject_ID == {}".format(subject_id)
    filter_table = question_table.query(query)
    return list(filter_table["Question"])


def get_trac_nghiem_info(subject_id):
    query = "Type == \"trac_nghiem\" and Subject_ID == {}".format(subject_id)
    return list(question_table.query(query)["Question"])


def get_tu_luan_info(subject_id):
    query = "Type == \"tu_luan\" and  Subject_ID == {}".format(subject_id)
    return list(question_table.query(query)["Question"])


def get_question_difficulty(question_id):
    query = "Question_ID == {}".format(question_id)
    return str(list(question_table.query(query)["Difficulty"])[0])


def get_question_chapter(question_id):
    query = "Question_ID == {}".format(question_id)
    return list(question_table.query(query)["Chapter"])[0]


def get_question_id_on_question_from_question_table(question):
    query = "Question == \"{}\"".format(question)
    query_data = list(question_table.query(query)["Question_ID"])
    if not query_data:
        print("there is no matching row")
    else:
        return list(question_table.query(query)["Question_ID"])[0]


def remove_question_from_question_table(question_id):
    from database.Exam.exam_question_access import remove_question_from_exam_question_table
    from database.MCQS_Answer.mcq_answer_access import remove_question_and_answer_from_mcq_answer_table
    from database.MCQS_Answer.written_exam_answer_access import remove_question_and_answer_from_written_exam_answer_table
    remove_question_and_answer_from_written_exam_answer_table(question_id)
    remove_question_and_answer_from_mcq_answer_table(question_id)
    remove_question_from_exam_question_table(question_id)
    query = "Question_ID == {}".format(question_id)
    question_table.drop(question_table.query(query).index, inplace=True)


def insert_question_to_question_table(question, subject_id, question_type, difficulty, chapter):
    last_question_id = question_table.iloc[-1, 0]
    question_table.loc[question_table.shape[0]] = [last_question_id + 1, question, subject_id,
                                                   question_type, difficulty, chapter]


def save_question_table():
    question_table.to_csv(QUESTION_PATH, index=False)


def get_question(question_id):
    try:
        query = "Question_ID == {}".format(question_id)
        return str(list(question_table.query(query)["Question"])[0])
    except IndexError:
        print(list(question_table.query(query)["Question"])[0])


def get_feasible_question_on_difficulty(subject_id, so_cau_de, so_cau_vua, so_cau_kho):
    query1 = "Subject_ID == {} and Difficulty == 1".format(subject_id)
    query2 = "Subject_ID == {} and Difficulty == 2".format(subject_id)
    query3 = "Subject_ID == {} and Difficulty == 3".format(subject_id)
    so_cau_de_index = list(question_table.query(query1).index)
    so_cau_vua_index = list(question_table.query(query2).index)
    so_cau_kho_index = list(question_table.query(query3).index)
    if len(so_cau_de_index) < so_cau_de:
        return False
    elif len(so_cau_vua_index) < so_cau_vua:
        return False
    elif len(so_cau_kho_index) < so_cau_kho:
        return False
    indexes = so_cau_de_index[:so_cau_de] + so_cau_vua_index[:so_cau_vua] + so_cau_kho_index[:so_cau_kho]
    question_ids = []
    for index in indexes:
        question_ids.append(question_table.loc[index]["Question_ID"])
    return question_ids


def get_feasible_question_on_coverage(subject_id, coverage):
    indexes = []
    for i, j in enumerate(coverage):
        query = "Subject_ID == {} and Chapter == {}".format(subject_id, i+1)
        chapter_index = list(question_table.query(query).index)
        if len(chapter_index) < j:
            return False
        indexes += chapter_index[:j]
    question_ids = []
    for index in indexes:
        question_ids.append(question_table.loc[index]["Question_ID"])
    return question_ids


def get_question_statistic(subject_id):
    difficulty = []
    for i in range(3):
        query = "Subject_ID == {} and Difficulty == {}".format(subject_id, i + 1)
        difficulty.append(question_table.query(query).shape[0])
    from database.Subject.subject_access import get_subject_chapter
    chapter = []
    for i in range(get_subject_chapter(subject_id)):
        query = "Subject_ID == {} and Chapter == {}".format(subject_id, i + 1)
        chapter.append(question_table.query(query).shape[0])
    return difficulty, chapter



















