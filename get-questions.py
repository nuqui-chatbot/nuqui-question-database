#we get the questions from http://www.jservice.io/ and load it into the question db

import sqlite3
import requests
import json
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

def get_question_and_save_into_db( category ):
    r = requests.get('http://www.jservice.io/api/category?id='+category)
    questions = r.json()['clues']

    for question in questions:
        cursor.execute('INSERT INTO downloaded_question(id, answer, question, value) VALUES (?, ?, ?, ?)',
                (question['id'], question['answer'], question['question'], question['value']))

    conn.commit()

categories = ['49', '253', '832', '1723', '15878']

for cat in categories:
        get_question_and_save_into_db(cat)
