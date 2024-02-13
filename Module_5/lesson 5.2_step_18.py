class AnyClass:
    def __init__(self, **kwargs) -> None:
        # self.__dict__ = kwargs
        self.__dict__.update(kwargs)

    def _format(self):
        return [f"{k}={repr(v)}" for k, v in self.__dict__.items()]

    def __str__(self) -> str:
        return f"{__class__.__name__}: {', '.join(self._format())}"

    def __repr__(self) -> str:
        return f"{__class__.__name__}({', '.join(self._format())})"


attrs = {
    "name": "Margaret Heafield Hamilton",
    "birth_date": "17.09.1936",
    "age": 86,
    "career": "computer scientist",
}
obj = AnyClass(**attrs)
print(obj)

attrs = {
    "name": "Guido van Rossum",
    "birth_date": "31.01.1956",
    "age": 67,
    "career": "python guru",
}
obj = AnyClass(**attrs)
print(obj.name)
print(obj.birth_date)
print(obj.age)
print(obj.career)
