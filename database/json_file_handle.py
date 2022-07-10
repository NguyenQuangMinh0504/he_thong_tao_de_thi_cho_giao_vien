import pandas as pd
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
    with open(fp, "r") as f:
        for index, table in f.readlines():
            list_table[index] = pd.read_json(table)
        save_exam_table()
        save_exam_question_table()
        save_mcq_answer_table()
        save_question_table()
        save_written_exam_answer_table()
        save_subject_table()
