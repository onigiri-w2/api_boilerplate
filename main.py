from abc import ABC, abstractmethod


class Parent:
    @abstractmethod
    def hoge(self) -> None:
        pass


class Child(Parent):
    # def hoge(self) -> None:
    #     print("ok")

    def boge(self) -> None:
        print("bg")


if __name__ == "__main__":
    Child()
