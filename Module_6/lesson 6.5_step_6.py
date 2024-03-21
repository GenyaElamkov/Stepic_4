class Greeter:
    def __init__(self, name) -> None:
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __enter__(self):
        print(f"Приветствую, {self.name}!")
        return self

    def __exit__(self, *args, **kwargs):
        print(f"До встречи, {self.name}!")


with Greeter("Кейв") as greeter:
    print(greeter.name)
