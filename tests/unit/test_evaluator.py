from freiburger_evaluator import evaluator, scale, respondent
import pytest


class TestEvaluator:
    @pytest.fixture(scope='function')
    def test_evaluator(self):
        test_raw_scale_1 = scale.Scale(
            number=1,
            name="Scale1",
            yanswers={1, 3},
            nanswers={2},
            standard_keys=[10, 20, 30]
        )
        test_raw_scale_2 = scale.Scale(
            number=2,
            name="Scale2",
            yanswers={2},
            nanswers={3},
            standard_keys=[15, 25, 35]
        )
        test_raw_scales = [test_raw_scale_1, test_raw_scale_2]
        test_answers = ['Да', 'Нет', 'Нет']
        test_respondent = respondent.Respondent(
            start_timestamp="2018/10/24 8:52:35 PM GMT+3",
            email="test@testmail.ru",
            name="test",
            date_of_birth="1987-10-23",
            date_of_test="2018-11-04",
            answers=test_answers,
            scales=test_raw_scales
        )
        return evaluator.Evaluator(
            respondent=test_respondent
        )

    def test_evaluate_raw_scores(self, test_evaluator):
        test_evaluator.evaluate_raw_scores()
        assert test_evaluator.respondent.scales[0].raw_score == 2
        assert test_evaluator.respondent.scales[1].raw_score == 1

    def test_evaluate_standard_scores(self, test_evaluator):
        test_evaluator.evaluate_raw_scores()
        test_evaluator.evaluate_standard_scores()
        assert test_evaluator.respondent.scales[0].standard_score == 30
        assert test_evaluator.respondent.scales[1].standard_score == 25

    def test_respondent_summary(self, test_evaluator):
        test_evaluator.evaluate_raw_scores()
        test_evaluator.evaluate_standard_scores()
        print(test_evaluator.respondent.compose_summary())
