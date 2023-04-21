from inspect import signature
from typing import Callable


class Evaluator:
    """バリデーターの評価条件を表すクラス
    Usage:
        ```
        e = Evaluator(lambda x, y: x < y)
        e.evaluate({'x': 1, 'y': 2}) # True
        ```
    """

    def __init__(self, formula: Callable[..., bool]):
        self._formula = formula
        self._args = [str(v) for v in signature(formula).parameters]

    def evaluate(self, key_value_map: dict) -> bool:
        """与えられた値一覧が評価条件を満たすかどうかを返す

        Args:
            key_value_map (dict): 値一覧。self._argsの要素が全て含まれている必要がある。

        Raises:
            ValueError: self._argsの要素が全て含まれていない場合

        Returns:
            bool: formulaの条件を満たすならTrue。つまり、与えられた値一覧が評価条件を満たすならTrue。合格。
        """
        if not all([k in key_value_map for k in self._args]):
            raise ValueError
        return self._formula(**{k: v for k, v in key_value_map.items() if k in self._args})
