class Cat:
    counter = 0

    def __init__(self, name: str, age: int | float) -> None:
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        __class__.counter += 1
        return self._name

    @property
    def age(self) -> int | float:
        return self._age

    @classmethod
    def counter_cat(cls) -> int:
        return cls.counter

    @staticmethod
    def get_age(age: int | float) -> int | float:
        """
        1- год == 15 человеческим
        2 - + 9 лет
        дальше + 4
        """
        one_year = 15
        two_year = 9
        next_year = 4
        res = 0
        if age == 1:
            res = one_year
        elif 1 < age <= 2:
            res = one_year + two_year
        else:
            res = one_year + two_year + next_year
        return res


cat_1 = Cat("Мурзик", 1)
print(cat_1.name)
print(cat_1.get_age(1))


cat_2 = Cat("Барсик", 2)
print(cat_2.name)
print(Cat.counter_cat())
