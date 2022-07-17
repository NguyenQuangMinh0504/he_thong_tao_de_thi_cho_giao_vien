import pandas as pd

import database.Exam.exam_access
from database.Exam.exam_access import exam_table, save_exam_table
from database.Exam.exam_question_access import exam_question_table, save_exam_question_table
from database.Question.question_access import question_table, save_question_table
from database.Answer.mcq_answer_access import mcq_answer_table, save_mcq_answer_table
from database.Answer.written_exam_answer_access import written_exam_answer_table, save_written_exam_answer_table
from database.Subject.subject_access import subject_table, save_subject_table

list_table = [exam_table, exam_question_table, question_table,
              mcq_answer_table, written_exam_answer_table, subject_table]


def export_all_to_json_file(fp):
    with open(fp, "w") as f:
        for i in list_table:
            f.write(i.to_json() + "\n")


def import_all_from_json_file(fp):
    f = open(fp, "r")
    database.Exam.exam_access.exam_table = pd.read_json(f.readline())
    database.Exam.exam_question_access.exam_question_table = pd.read_json(f.readline())
    database.Question.question_access.question_table = pd.read_json(f.readline())
    database.Answer.mcq_answer_access.mcq_answer_table = pd.read_json(f.readline())
    database.Answer.written_exam_answer_access.written_exam_answer_table = pd.read_json(f.readline())
    database.Subject.subject_access.subject_table = pd.read_json(f.readline())
    save_exam_table()
    save_exam_question_table()
    save_mcq_answer_table()
    save_question_table()
    save_written_exam_answer_table()
    save_subject_table()
