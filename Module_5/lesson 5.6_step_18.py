class SortKey:
    def __init__(self, *args) -> None:
        self.args = args

    def __call__(self, object):
        return [getattr(object, k) for k in self.args]


# user = SortKey("name", 'age')
# print(user.args)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"User({self.name}, {self.age})"


users = [
    User("Gvido", 67),
    User("Timur", 30),
    User("Arthur", 20),
    User("Timur", 45),
    User("Gvido", 60),
]

print(sorted(users, key=SortKey("name")))
print(sorted(users, key=SortKey("name", "age")))
print(sorted(users, key=SortKey("age")))
print(sorted(users, key=SortKey("age", "name")))

# [User(Arthur, 20), User(Gvido, 67), User(Gvido, 60), User(Timur, 30), User(Timur, 45)]
# [User(Arthur, 20), User(Gvido, 60), User(Gvido, 67), User(Timur, 30), User(Timur, 45)]
# [User(Arthur, 20), User(Timur, 30), User(Timur, 45), User(Gvido, 60), User(Gvido, 67)]
# [User(Arthur, 20), User(Timur, 30), User(Timur, 45), User(Gvido, 60), User(Gvido, 67)]