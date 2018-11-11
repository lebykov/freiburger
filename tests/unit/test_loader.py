import pytest
import csv
import json
from freiburger_evaluator import loader


class TestFreiburgerLoader:
    def test_freiburger_loader(self, tmpdir):
        test_scales_file = tmpdir.join('test_scales_freiburger.json')
        test_answers_file = tmpdir.join('test_answers_freiburger.csv')
        print(f'scales path: {test_scales_file.realpath()}')
        print(f'answers path: {test_answers_file.realpath()}')

        scales_path = test_scales_file.realpath()
        answers_path = test_answers_file.realpath()

        test_scales_freiburger = [
            {
                "number": 1,
                "name": "Scale1",
                "yanswers": [1, 3],
                "nanswers": [2],
                "standard_keys": [10, 20, 30]
            },
            {
                "number": 2,
                "name": "Scale2",
                "yanswers": [2],
                "nanswers": [3],
                "standard_keys": [15, 25, 35]
            }
        ]

        test_headers = ["Отметка времени", "Имя пользователя", "Фамилия Имя Отчество", "Дата рождения",
                   "Дата заполнения теста", "Вопрос 1", "Вопрос 2", "Вопрос 3"]
        test_person_answers = ["2018/11/11 12:34:56 AM GMT+3", "test@testmail.ru", "Антон",
                               "1965-08-10", "2018-11-11", 'Да', 'Нет', 'Нет']

        with open(scales_path, 'w') as sf, open(answers_path, 'w', newline='') as af:
            json.dump(test_scales_freiburger, sf)
            spamwriter = csv.writer(af)
            spamwriter.writerow(test_headers)
            spamwriter.writerow(test_person_answers)

        print(f'content scales: {test_scales_file.read()}')
        print(f'content answers: {test_answers_file.read()}')

        test_loader = loader.Loader.factory('frei', str(test_answers_file), str(test_scales_file))

        # todo: implement proper verification for loaded respondent - research on __eq__ and __cmp__
        print(test_loader.load_respondents())


class TestCatLoader:
    def test_cat_loader(self, tmpdir):
        test_scales_file = tmpdir.join('test_scales_cat.json')
        test_answers_file = tmpdir.join('test_answers_cat.csv')
        print(f'scales path: {test_scales_file.realpath()}')
        print(f'answers path: {test_answers_file.realpath()}')

        scales_path = test_scales_file.realpath()
        answers_path = test_answers_file.realpath()

        test_scales_cat = [
            {
                "number": 1,
                "name": "Scale1",
                "aanswers": [1, 3],
                "banswers": [2]
            },
            {
                "number": 2,
                "name": "Scale2",
                "aanswers": [2],
                "banswers": [3]
            }
        ]

        test_headers = ["Отметка времени", "Имя пользователя", "Фамилия Имя Отчество", "Дата рождения",
                   "Дата заполнения теста", "Вопрос 1", "Вопрос 2", "Вопрос 3"]
        test_person_answers = ["2018/11/11 12:34:56 AM GMT+3", "test@testmail.ru", "Антон",
                               "1965-08-10", "2018-11-11", 'а', 'б', 'б']

        with open(scales_path, 'w') as sf, open(answers_path, 'w', newline='') as af:
            json.dump(test_scales_cat, sf)
            spamwriter = csv.writer(af)
            spamwriter.writerow(test_headers)
            spamwriter.writerow(test_person_answers)

        print(f'content scales: {test_scales_file.read()}')
        print(f'content answers: {test_answers_file.read()}')

        test_loader = loader.Loader.factory('cat', str(test_answers_file), str(test_scales_file))

        # todo: implement proper verification for loaded respondent - research on __eq__ and __cmp__
        print(test_loader.load_respondents())
