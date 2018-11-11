import csv
import json
from freiburger_evaluator import respondent, scale


class Loader(object):
    def __init__(self, answers_file, scales_file):
        self.answers_file = answers_file
        self.scales_file = scales_file
        self.scales = []
        self.validate = False

    def load_respondents(self):
        self.scales = self._load_scales()
        print(f'Загрузил таблицу с {len(self.scales)} шкалами')
        with open(self.answers_file, encoding="utf8", newline='') as f:
            respondents = []
            reader = csv.reader(f)
            for n, row in enumerate(reader):
                # skip first line since it contains table headers
                if n == 0:
                    continue
                user_info = row[:5]
                user_answers = row[5:]
                # check if answers array contains valid elements
                # think about necessity of this check
                if self.validate:
                    self._validate_answers(user_answers)
                r = respondent.Respondent(
                    start_timestamp=user_info[0],
                    email=user_info[1],
                    name=user_info[2],
                    date_of_birth=user_info[3],
                    date_of_test=user_info[4],
                    answers=user_answers,
                    scales=self.scales
                )
                respondents.append(r)
                # print("added new respondent")
                # print(r)
                # print('\n')
            return respondents

    def _load_scales(self):
        raise NotImplementedError

    def _validate_answers(self, answers):
        raise NotImplementedError

    @staticmethod
    def factory(loader_name, answers_file, scales_file):
        if loader_name == 'frei':
            return FreiburgerLoader(answers_file, scales_file)
        elif loader_name == 'cat':
            return CatLoader(answers_file, scales_file)


class FreiburgerLoader(Loader):
    def _load_scales(self):
        with open(self.scales_file, 'r') as f:
            scales = []
            for obj in json.load(f):
                s = scale.Scale.factory(
                    scale_name='frei',
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

    def _validate_answers(self, answers):
        assert len(answers) == 114
        # print(f'number of empty answers: {answers.count("")}')
        # print(f'number of Да  answers: {answers.count("Да")}')
        # print(f'number of Нет answers: {answers.count("Нет")}')
        unique_answers = set(answers)
        # print(unique_answers)
        assert len(unique_answers) in {2, 3}
        assert 'Да' in unique_answers
        assert 'Нет' in unique_answers


class CatLoader(Loader):
    def _load_scales(self):
        with open(self.scales_file, 'r') as f:
            scales = []
            for obj in json.load(f):
                s = scale.Scale.factory(
                    scale_name='cat',
                    number=obj["number"],
                    name=obj["name"],
                    aanswers={*obj["aanswers"]},
                    banswers={*obj["banswers"]}
                )
                scales.append(s)
                # print("added new scale")
                # print(s)
                # print('\n')
            return scales

    def _validate_answers(self, answers):
        assert len(answers) == 126
        # print(f'number of empty answers: {answers.count("")}')
        # print(f'number of Да  answers: {answers.count("Да")}')
        # print(f'number of Нет answers: {answers.count("Нет")}')
        unique_answers = set(answers)
        # print(unique_answers)
        assert len(unique_answers) == 2
        assert 'а' in unique_answers
        assert 'б' in unique_answers
