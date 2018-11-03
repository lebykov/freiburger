class Respondent:
    def __init__(self, start_timestamp, email, name, date_of_birth, date_of_test, answers):
        self.start_timestamp = start_timestamp,
        self.email = email,
        self.name = name,
        self.date_of_birth = date_of_birth,
        self.date_of_test = date_of_test,
        self.answers = answers

    def __repr__(self):
        return f'Respondent: (start_timestamp={self.start_timestamp}), ' \
               f'email={self.email}, name={self.name}, ' \
               f'date_of_birth={self.date_of_birth}, date_of_test={self.date_of_test}, ' \
               f'answers={self.answers})'
