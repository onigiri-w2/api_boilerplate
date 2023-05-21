"""
現状、クエリの基底クラスは存在しない。
けど、クエリのクラスで定義するメソッドの返り値は、全てMethodReturnTypeかMethodReturnListTypeに統一した方が使いやすくなると思う。

Usage:
    from src.rdb.interface.query import MethodReturnListType, MethodReturnType

    class UserQuery:
        @classmethod
        def all(cls) -> MethodReturnListType:
            ...
"""
from typing import Any, Dict, List

MethodReturnType = Dict[str, Any]
MethodReturnListType = List[Dict[str, Any]]
