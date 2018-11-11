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

    def __repr__(self):
        return f'Respondent (\n\tstart_timestamp={self.start_timestamp}), ' \
               f'\n\temail={self.email}, \n\tname={self.name}, ' \
               f'\n\tdate_of_birth={self.date_of_birth}, \n\tdate_of_test={self.date_of_test}, ' \
               f'\n\tanswers={self.answers}, \n\tscales={self.scales})'

