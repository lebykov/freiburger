import csv
import sys
from freiburger_evaluator import respondent, scale
import json


def load_respondents(answers_file):
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
                answers=user_answers
            )
            respondents.append(r)
            print("added new respondent")
            print(r)
            print('\n\n\n')
        return respondents


def load_scales(scales_file):
    with open(scales_file, 'r') as f:
        scales = []
        for obj in json.load(f):
            s = scale.Scale(
                number=obj["number"],
                name=obj["name"],
                yanswers={*obj["yanswers"]},
                nanswers={*obj["nanswers"]}
            )
            scales.append(s)
            print("added new scale")
            print(s)
            print('\n\n\n')
        return scales


def main(answers_file, scales_file):
    loaded_respondents = load_respondents(answers_file)
    print(f'laded {len(loaded_respondents)} respondents')
    loaded_scales = load_scales(scales_file)
    print(f'laded {len(loaded_scales)} scales')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
