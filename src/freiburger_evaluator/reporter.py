class Reporter(object):
    def __init__(self, respondent):
        self.respondent = respondent

    @staticmethod
    def factory(reporter_name, respondent):
        if reporter_name == 'frei':
            return FreiburgerReporter(respondent)


class FreiburgerReporter(Reporter):
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
                  f'Дата тестирования: {self.respondent.date_of_test}\nФИО: {self.respondent.name}\n' \
                  f'email: {self.respondent.email}\nДата рожденя: {self.respondent.date_of_birth}\n' \
                  f'Баллы по стандартной шкале\n' \
                  f'{number_literal:^{number_col_width}} {name_literal:^{name_col_width}} {raw_literal:^{raw_col_width}} {score_literal:^{score_col_width}}\n'

        for scale in self.respondent.scales:
            summary += f'{scale.number:>{number_col_width}} {scale.name:<{name_col_width}} {scale.raw_score:>{raw_col_width}} {scale.standard_score:>{score_col_width}}\n'

        return summary
