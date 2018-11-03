import csv
import sys


def main(answers_file):
    with open(answers_file, encoding="utf8", newline='') as f:
        reader = csv.reader(f)
        # reader = csv.DictReader(f)
        for row in reader:
            print(f'user info: {row[:5]}')
            user_answers = row[5:]
            print(f'user answers({len(user_answers)}): {user_answers}')


if __name__ == '__main__':
    main(sys.argv[1])
