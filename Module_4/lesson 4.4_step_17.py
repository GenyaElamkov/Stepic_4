class User:
    def __init__(self, name: str, age: int) -> None:
        self._name = self.set_name(name)
        self._age = self.set_age(age)

    def get_name(self) -> str:
        return self._name

    def set_name(self, new_name: str) -> str | ValueError:
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
            return self._name
        raise ValueError("Некорректное имя")

    def get_age(self) -> str:
        return self._age

    def set_age(self, new_age: int) -> int | ValueError:
        if isinstance(new_age, int) and 0 <= new_age <= 110:
            self._age = new_age
            return self._age
        raise ValueError("Некорректный возраст")


user = User("Меган", 37)

invalid_names = (-1, True, "", [], "123456", "Меган906090")

for name in invalid_names:
    try:
        user.set_name(name)
    except ValueError as e:
        print(e)
