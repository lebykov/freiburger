class Evaluator:
    def __init__(self, respondent):
        self.respondent = respondent

    def evaluate_raw_scores(self):
        # print(f'\nevaluate_raw_scores()')
        # print(f'\tanswers:{self.respondent.answers}')
        # print(f'\tscales: {self.respondent.scales}')
        for num, ans in enumerate(self.respondent.answers):
            # print(f'\tnum, ans: {num}, {ans}')
            for scale in self.respondent.scales:
                # print(f'\tscale:{scale}')
                scale.check_answer(num + 1, ans)

    def evaluate_standard_scores(self):
        for scale in self.respondent.scales:
            scale.convert_to_standard()
