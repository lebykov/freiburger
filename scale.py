class Scale:
    def __init__(self, number, name, yanswers, nanswers):
        self.number = number
        self.name = name
        self.yanswers = yanswers
        self.nanswers = nanswers
        self.score = 0

    def __repr__(self):
        return f'Scale({self.name}, {self.number}, {self.yanswers}, {self.nanswers}, {self.score}'

    def check_answer(self, question_numbers, answer):
        if answer == 'Да' and question_numbers in self.yanswers:
            self.score += 1
        if answer == 'Нет' and question_numbers in self.nanswers:
            self.score += 1
