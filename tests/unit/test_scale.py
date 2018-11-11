import pytest
from freiburger_evaluator import scale


class TestScale:

    def test_freiburger_check_answer(self):
        test_scale = scale.Scale.factory(
            scale_name='frei',
            number='1',
            name='Test',
            yanswers={1, 3},
            nanswers={2},
            standard_keys={}
        )

        assert test_scale.raw_score == 0
        test_scale.check_answer(1, 'Да')
        assert test_scale.raw_score == 1
        test_scale.check_answer(2, 'Нет')
        assert test_scale.raw_score == 2
        test_scale.check_answer(3, 'Нет')
        assert test_scale.raw_score == 2
        test_scale.check_answer(2, 'Да')
        assert test_scale.raw_score == 2
        test_scale.check_answer(4, 'Да')
        assert test_scale.raw_score == 2
        test_scale.check_answer(2, 'Не знаю')
        assert test_scale.raw_score == 2

    def test_cat_check_answer(self):
        test_scale = scale.Scale.factory(
            scale_name='cat',
            number='1',
            name='Test',
            aanswers={1, 3},
            banswers={2}
        )
        assert test_scale.raw_score == 0
        test_scale.check_answer(1, 'а')
        assert test_scale.raw_score == 1
        test_scale.check_answer(2, 'б')
        assert test_scale.raw_score == 2
        test_scale.check_answer(3, 'б')
        assert test_scale.raw_score == 2
        test_scale.check_answer(2, 'а')
        assert test_scale.raw_score == 2
        test_scale.check_answer(4, 'а')
        assert test_scale.raw_score == 2
        test_scale.check_answer(2, 'в')
        assert test_scale.raw_score == 2

