from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    surname: str
    age: int = field(init=True)


person1 = Person('Гвидо', 'ван Россум', 67)
person2 = Person('Гвидо', 'ван Россум', 68)

print(person1 == person2)