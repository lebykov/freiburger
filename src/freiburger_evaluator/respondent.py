import copy


class Respondent:
    def __init__(self, start_timestamp, email, name, date_of_birth, date_of_test, answers, scales):
        self.start_timestamp = start_timestamp
        self.email = email
        self.name = name
        self.date_of_birth = date_of_birth
        self.date_of_test = date_of_test
        self.answers = answers
        self.scales = copy.deepcopy(scales)
        self.check_default_scores()

    def __repr__(self):
        return f'Respondent (\n\tstart_timestamp={self.start_timestamp}), ' \
               f'\n\temail={self.email}, \n\tname={self.name}, ' \
               f'\n\tdate_of_birth={self.date_of_birth}, \n\tdate_of_test={self.date_of_test}, ' \
               f'\n\tanswers={self.answers}, \n\tscales={self.scales})'

    def compose_summary(self):
        number_literal = '#'
        name_literal = 'Название шкалы'
        raw_literal = 'Сырые'
        score_literal = 'Баллы'
        number_col_width = 3
        name_col_width = 26
        raw_col_width = 5
        score_col_width = 5
        summary = f'********************************************************\n' \
                  f'Результаты обработки Фрайбургского личностного опросника\n' \
                  f'********************************************************\n' \
                  f'Дата тестирования: {self.date_of_test}\nФИО: {self.name}\n' \
                  f'email: {self.email}\nДата рожденя: {self.date_of_birth}\n' \
                  f'Баллы по стандартной шкале\n' \
                  f'{number_literal:^{number_col_width}} {name_literal:^{name_col_width}} {raw_literal:^{raw_col_width}} {score_literal:^{score_col_width}}\n'

        for scale in self.scales:
            summary += f'{scale.number:>{number_col_width}} {scale.name:<{name_col_width}} {scale.raw_score:>{raw_col_width}} {scale.standard_score:>{score_col_width}}\n'

        return summary

    def check_default_scores(self):
        for scale in self.scales:
            assert scale.raw_score == 0
            assert scale.standard_score == 0


