class Scale(object):
    @staticmethod
    def factory(scale_name, **kwargs):
        if scale_name == 'frei':
            return FreiburgerScale(**kwargs)
        elif scale_name == 'cat':
            return CatScale(**kwargs)


class FreiburgerScale(Scale):
    def __init__(self, number, name, yanswers, nanswers, standard_keys):
        super().__init__()
        self.number = number
        self.name = name
        self.yanswers = yanswers
        self.nanswers = nanswers
        self.standard_keys = standard_keys
        self.raw_score = 0
        self.standard_score = 0
        self._check_defaults()

    def __repr__(self):
        return f'Scale(\n\tname={self.name}, \n\tnumber={self.number}, \n\tyanswers={self.yanswers}, ' \
               f'\n\tnanswers={self.nanswers}, \n\tstandard_keys={self.standard_keys}, ' \
               f'\n\traw_score={self.raw_score}, \n\tstandard_score={self.standard_score})'

    def check_answer(self, question_numbers, answer):
        if answer == 'Да' and question_numbers in self.yanswers:
            self.raw_score += 1
        if answer == 'Нет' and question_numbers in self.nanswers:
            self.raw_score += 1

    def convert_to_standard(self):
        self.standard_score = self.standard_keys[self.raw_score]

    def _check_defaults(self):
        assert self.raw_score == 0
        assert self.standard_score == 0


class CatScale(Scale):
    def __init__(self, number, name, aanswers, banswers):
        super().__init__()
        self.number = number
        self.name = name
        self.aanswers = aanswers
        self.banswers = banswers
        self.raw_score = 0

    def __repr__(self):
        return f'Scale(\n\tname={self.name}, \n\tnumber={self.number}, \n\taanswers={self.aanswers}, ' \
               f'\n\tbanswers={self.banswers}, \n\traw_score={self.raw_score}'

    def check_answer(self, question_numbers, answer):
        if answer == 'а' and question_numbers in self.aanswers:
            self.raw_score += 1
        if answer == 'б' and question_numbers in self.banswers:
            self.raw_score += 1

    def _check_defaults(self):
        assert self.raw_score == 0
