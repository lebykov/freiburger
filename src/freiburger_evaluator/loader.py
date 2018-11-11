import csv
import json
import random
from freiburger_evaluator import respondent, scale


class Loader(object):
    def __init__(self, answers_file, scales_file):
        self.answers_file = answers_file
        self.scales_file = scales_file
        self.scales = []

    def load_respondents(self):
        self.scales = self._load_scales(self.scales_file)
        print(f'Загрузил таблицу с {len(self.scales)} шкалами')
        with open(self.answers_file, encoding="utf8", newline='') as f:
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
                    scales=self.scales
                )
                respondents.append(r)
                # print("added new respondent")
                # print(r)
                # print('\n')
            return respondents

    def _load_scales(self, scales_file):
        raise NotImplementedError

    @staticmethod
    def factory(loader_name, answers_file, scales_file):
        if loader_name == 'frei':
            return FreiburgerLoader(answers_file, scales_file)


class FreiburgerLoader(Loader):
    def _load_scales(self, scales_file):
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

