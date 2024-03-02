class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, attr):
        if attr == "total":
            return self.price * self.quantity
        elif attr == "name":
            return self.__dict__[attr].title()
        return object.__getattribute__(self, attr)


fruit = Item('banana', 15, 5)

print(fruit.price)
print(fruit.quantity)


fruit = Item("banana", 15, 5)

print(fruit.name)
print(fruit.total)

course = Item('pygen', 3900, 2)

print(course.name)
print(course.price)
print(course.quantity)
print(course.total)
