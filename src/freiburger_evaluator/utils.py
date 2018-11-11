import csv
import json
import random
from freiburger_evaluator import respondent, scale


def load_respondents(answers_file, scales):
    with open(answers_file, encoding="utf8", newline='') as f:
        respondents = []
        reader = csv.reader(f)
        for row in reader:
            user_info = row[:5]
            user_answers = row[5:]
            r = respondent.Respondent(
                start_timestamp=user_info[0],
                email=user_info[1],
                name=user_info[2],
                date_of_birth=user_info[3],
                date_of_test=user_info[4],
                answers=user_answers,
                scales=scales
            )
            respondents.append(r)
            # print("added new respondent")
            # print(r)
            # print('\n')
        return respondents


def load_scales(scales_file):
    with open(scales_file, 'r') as f:
        scales = []
        for obj in json.load(f):
            s = scale.Scale(
                number=obj["number"],
                name=obj["name"],
                yanswers={*obj["yanswers"]},
                nanswers={*obj["nanswers"]},
                standard_keys=obj["standard_keys"]
            )
            scales.append(s)
            # print("added new scale")
            # print(s)
            # print('\n')
        return scales


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
