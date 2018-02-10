import sqlite3
import requests
import json
import random

conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

def get_question_and_save_into_db( category ):
    questions_path = "quizduellFragen.csv"

    questions_file = open(questions_path, 'r')

    for question in questions_file:
        question_list = question.split(";")
        cursor.execute('INSERT INTO downloaded_question(id, answer, question, value) VALUES (?, ?, ?, ?)',
                (question['id'], question['answer'], question['question'], question['value']))

    conn.commit()


def random_value():
    return 100 * random.randint(1,3)


