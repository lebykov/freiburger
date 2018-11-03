import pytest
from freiburger_evaluator import scale


class TestScale:

    def test_check_answer(self):
        test_scale = scale.Scale(
            number='1',
            name='Test',
            yanswers={1, 3},
            nanswers={2}
        )

        assert test_scale.score == 0
        test_scale.check_answer(1, 'Да')
        assert test_scale.score == 1
        test_scale.check_answer(2, 'Нет')
        assert test_scale.score == 2
        test_scale.check_answer(3, 'Нет')
        assert test_scale.score == 2
        test_scale.check_answer(2, 'Да')
        assert test_scale.score == 2
        test_scale.check_answer(4, 'Да')
        assert test_scale.score == 2
        test_scale.check_answer(2, 'Не знаю')
        assert test_scale.score == 2

