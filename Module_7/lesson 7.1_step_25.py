class Animal:
    def sleep(self): ...

    def eat(self): ...


class Fish(Animal):
    def swim(self): ...


class Bird(Animal):
    def lay_eggs(self): ...


class FlyingBird(Bird):
    def fly(self): ...


# INPUT DATA:

# TEST_1:
print(issubclass(Fish, Animal))
print(issubclass(Bird, Animal))
print(issubclass(FlyingBird, Animal))
print(issubclass(FlyingBird, Bird))

# TEST_2:
animal = Animal()

print(animal.sleep())
print(animal.eat())

# TEST_3:
fish = Fish()

print(fish.sleep())
print(fish.eat())
print(fish.swim())

# TEST_4:
bird = Bird()
print(bird.sleep())
print(bird.eat())
print(bird.lay_eggs())

# TEST_5:
flying_bird = FlyingBird()
print(flying_bird.sleep())
print(flying_bird.eat())
print(flying_bird.lay_eggs())
print(flying_bird.fly())

# TEST_6:
animal = Animal()

methods = ["swim", "lay_eggs", "fly"]
for method in methods:
    print(hasattr(animal, method))
