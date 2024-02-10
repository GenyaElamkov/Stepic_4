class Pet:
    arr = []

    def __init__(self, name=None) -> None:
        self.name = name
        __cla.arr.append(self)

    @classmethod
    def first_pet(cls):
        try:
            return cls.arr[0]
        except IndexError:
            return None

    @classmethod
    def last_pet(cls):
        try:
            return cls.arr[-1]
        except IndexError:
            return None

    @classmethod
    def num_of_pets(cls):
        return len(cls.arr)


print(Pet.first_pet())
print(Pet.last_pet())
print(Pet.num_of_pets())

pet1 = Pet("Ratchet")
pet2 = Pet("Clank")
pet3 = Pet("Rivet")

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())
