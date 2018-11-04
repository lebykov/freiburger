class Scale:
    def __init__(self, number, name, yanswers, nanswers, standard_keys):
        self.number = number
        self.name = name
        self.yanswers = yanswers
        self.nanswers = nanswers
        self.standard_keys = standard_keys
        self.raw_score = 0
        self.standard_score = 0

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
