from typing import Dict, List, Tuple, TypeVar

from src.utils.validation.evaluator import Evaluator

T = TypeVar("T")


class Validator:
    """バリデーター

    事前に属性セットごとの評価条件（`Evaluator`）を登録しておき、その評価条件を満たせない場合はFalseが返ってくる仕様。

    Usage:
        from src.utils.validation.evaluator import Evaluator
        from src.utils.validation.validator import Validator

        class User:
            VALID_SCHEMA = [
                (Evaluator(lambda name: len(name) <= 20), "名前は20文字以内にしてください"),
                (Evaluator(lambda age: age >= 0), "年齢は0以上にしてください"),
                (Evaluator(lambda age, name: len(name) < age), "名前の長さは年齢より短くしてください"),
            ]

            def __init__(self, name: str, age: int):
                validator = Validator(self.VALID_SCHEMA)
                if not validator.validate({"name": name, "age": age}):
                    print(validator.errors)
                    # 例外を投げるなどして処理を中断する
                self.name = name
                self.age = age

        user = User('h'*21, -1)
        # 以下のようなエラーメッセージが出力される
        # ['名前は20文字以内にしてください', '年齢は0以上にしてください', '名前の長さは年齢より短くしてください']
    """

    def __init__(self, schema: List[Tuple[Evaluator, T]]):
        """バリデーターを初期化する

        Args:
            schema (List[Tuple[Evaluator, T]]): 評価条件とその条件に反した場合に出力されるオブジェクトの一覧
        """
        self._evaluator_errmsg_map = {evaluator: errmsg for evaluator, errmsg in schema}
        self._errors: List[T] = []

    def validate(self, key_value_map: Dict[str, T]) -> bool:
        """与えられた値一覧が評価条件を全て満たすかどうかを返す

        Args:
            key_value_map (Dict[str, Any]): 評価対象の値一覧

        Returns:
            bool: 評価条件を全て満たす場合はTrue、1つでも満たさない場合はFalse
        """
        for evaluator, errmsg in self._evaluator_errmsg_map.items():
            if not evaluator.evaluate(key_value_map):
                self._errors.append(errmsg)
        return len(self._errors) == 0

    @property
    def errors(self) -> List[T]:
        return self._errors
