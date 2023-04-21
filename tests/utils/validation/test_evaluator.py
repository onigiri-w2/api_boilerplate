import pytest

from src.utils.validation.evaluator import Evaluator


def describe_Evaluator():
    def describe_constructor():
        def test_インスタンス化():
            sut = Evaluator(lambda a, b: a > b)
            assert sut._args == ["a", "b"]

    def describe_evaluate():
        def test_与えられた値一覧が評価条件を満たす場合はTrueが返る():
            sut = Evaluator(lambda a, b: a > b)
            assert sut.evaluate({"a": 1, "b": 0})

        def test_与えられた値一覧が評価条件を満たさない場合はFalseが返る():
            sut = Evaluator(lambda a, b: a > b)
            assert not sut.evaluate({"a": 0, "b": 1})

        def test_評価条件の引数の順番が違ってもTrueが返る():
            sut = Evaluator(lambda b, a: a > b)
            assert sut.evaluate({"a": 1, "b": 0})

        def test_与えられた値一覧に評価条件に必要な値が含まれていない場合はValueErrorが発生する():
            sut = Evaluator(lambda a, b: a > b)
            with pytest.raises(ValueError):
                sut.evaluate({"a": 1})
