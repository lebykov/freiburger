import csv
import random


def generate_dummy_answers(file_name):
    with open(file_name, 'w', newline='') as f:
        spamwriter = csv.writer(f)
        headers = ["Отметка времени", "Имя пользователя", "Фамилия Имя Отчество", "Дата рождения",
                   "Дата заполнения теста", ]
        person_answers = ["2018/11/11 12:34:56 AM GMT+3", "test@testmail.ru", "Антон", "1965-08-10", "2018-11-11"]

        for i in range(126):
            headers.append(f'Вопрос {i + 1}')
            person_answers.append(random.choice(['а', 'б']))

        spamwriter.writerow(headers)
        spamwriter.writerow(person_answers)
