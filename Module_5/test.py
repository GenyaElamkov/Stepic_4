"""
Копилка
- положил 
- взял из
- сколько всего  
"""

from typing import Any, Iterator


class Boncnote:
    """Блокнота"""
    __slots__ = ("_nominall", "_name")

    def __init__(self, nominall: int, name: str = "rub") -> None:
        self.nominall = nominall
        self.name = name

    @property
    def nominall(self) -> str:
        return self._nominall

    @nominall.setter
    def nominall(self, __value) -> object | ValueError:
        if isinstance(__value, (int, float)):
            self._nominall = __value
        else:
            raise ValueError("Не правильный формат номинала")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, __value: str) -> None:
        if isinstance(__value, str):
            self._name = __value

    def __repr__(self) -> str:
        return f"{__class__.__name__}{self.nominall, self.name}"

    def __delattr__(self, __name: str) -> None:
        raise AttributeError("Удаление атрибута невозможно")
    
    def __hash__(self) -> int:
        return hash((self.nominall, self.name))


class Bunk:
    """Банк (корзина)"""
    __slots__ = "__bunks"

    def __init__(self, *boncnote: Boncnote) -> None:
        self.__bunks = []
        self.__bunks.extend(boncnote)

    def __repr__(self) -> str:
        return f"{__class__.__name__}({self.bunks})"

    def __len__(self) -> int:
        return len(self.bunks)
    
    def __iter__(self) -> Iterator:
        return iter(self.bunks)

    def __container__(self, item) -> bool:
        return item in self.bunks
    
    @property
    def bunks(self) -> list:
        return self.__bunks

    @property
    def summa(self) -> int | float:
        return sum(elem.nominall for elem in self.bunks)

    def subs(self, value):
        # if not isinstance(value, __class__):
        #     return NotImplemented
        del self.bunks[value.index()]

if __name__ == "__main__":
    hundry = Boncnote(100)
    fifty = Boncnote(50)
    sixtyn = Boncnote(60)
    ten = Boncnote(10)
    bunk = Bunk(hundry, fifty, sixtyn)
    # for elem in bunk:
    #     print(elem)
    # print(hasattr(bunk, ))
    print(ten in bunk)
    print(bunk.bunks)
    print(bunk.subs(fifty))
    print(bunk.bunks)