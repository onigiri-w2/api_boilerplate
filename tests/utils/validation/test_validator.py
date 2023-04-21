from src.utils.validation.validator import Validator


def describe_Validator():
    def describe_constructor():
        def test_インスタンス化(mocker):
            """
            Note: 内部プロパティを評価するのは良くないかも
            """
            mock_ev, mock_ev2 = mocker.Mock(), mocker.Mock()
            mock_ev.evaluate.return_value = True
            mock_ev2.evaluate.return_value = True
            schema = [(mock_ev, "error1"), (mock_ev2, "error2")]
            sut = Validator(schema)
            expect_map = {mock_ev: "error1", mock_ev2: "error2"}
            assert sut._evaluator_errmsg_map == expect_map
            assert sut._errors == []

    def describe_valiadte():
        def test_与えられた値一覧が評価条件を全て満たす場合はTrueが返る(mocker):
            mock_ev, mock_ev2 = mocker.Mock(), mocker.Mock()
            mock_ev.evaluate.return_value = True
            mock_ev2.evaluate.return_value = True
            schema = [(mock_ev, "error1"), (mock_ev2, "error2")]
            sut = Validator(schema)
            assert sut.validate({"a": 1, "b": 0})
            assert sut._errors == []

        def test_与えられた値一覧が評価条件を1つでも満たさない場合はFalseが返る(mocker):
            mock_ev, mock_ev2 = mocker.Mock(), mocker.Mock()
            mock_ev.evaluate.return_value = False
            mock_ev2.evaluate.return_value = True
            schema = [(mock_ev, "error1"), (mock_ev2, "error2")]
            sut = Validator(schema)
            assert not sut.validate({"a": 1, "b": 0})
            assert sut._errors == ["error1"]

        def test_与えられた値一覧が評価条件を全て満たさない場合はFalseが返る(mocker):
            mock_ev, mock_ev2 = mocker.Mock(), mocker.Mock()
            mock_ev.evaluate.return_value = False
            mock_ev2.evaluate.return_value = False
            schema = [(mock_ev, "error1"), (mock_ev2, "error2")]
            sut = Validator(schema)
            assert not sut.validate({"a": 1, "b": 0})
            assert sut._errors == ["error1", "error2"]

        def test_評価条件が無い場合はTrueが返る(mocker):
            sut = Validator([])
            assert sut.validate({"a": 1, "b": 0})
            assert sut._errors == []
