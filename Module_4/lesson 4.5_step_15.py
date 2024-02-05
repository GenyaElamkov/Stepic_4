class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def get_fullname(self) -> str:
        return f"{self.name} {self.surname}"

    def set_fullname(self, fullnames):
        self.name, self.surname = fullnames.split()

    fullname = property(get_fullname, set_fullname)


person = Person('Джон', 'Маккарти')

person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)