class Item:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name}, {self.price}$"


class ShoppingCart:
    def __init__(self, items: Item = []) -> None:
        self.items = items

    def add(self, name):
        self.items.append(name)

    def total(self):
        return sum(map(lambda item: item.price, self.items))

    def remove(self, name):
        self.items = [item for item in self.items if item.name != name]

    def __str__(self) -> str:
        return '\n'.join(str(item) for item in self.items)
# INPUT DATA:

# TEST_1:
item1 = Item("Yoga Mat", 130)
item2 = Item("Flannel Shirt", 22)

print(item1)
print(item2)

# TEST_2:
shopping_cart = ShoppingCart([Item("Yoga Mat", 130)])

shopping_cart.add(Item("Flannel Shirt", 22))
print(shopping_cart)
print(shopping_cart.total())

# TEST_3:
shopping_cart = ShoppingCart([Item("Yoga Mat", 130), Item("Flannel Shirt", 22)])

shopping_cart.remove("Yoga Mat")
print(shopping_cart)
print(shopping_cart.total())

# TEST_4:
shopping_cart = ShoppingCart(
    [
        Item("Banana", 100),
        Item("Apple", 120),
        Item("Orange", 110),
        Item("Tomato", 180),
        Item("Cucumber", 150),
    ]
)

shopping_cart.add(Item("Banana", 100))
print(shopping_cart)
print(shopping_cart.total())

shopping_cart.remove("Banana")
print(shopping_cart)
print(shopping_cart.total())

# TEST_5:
shopping_cart = ShoppingCart()
print(shopping_cart)
