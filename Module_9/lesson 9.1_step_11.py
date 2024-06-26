    """
    Это определение класса для объекта Selfie, который может сохранять и восстанавливать состояния. 
    Вот, что делает каждый метод:

    __init__(self): Инициализирует объект Selfie пустым словарем save_obj и ключом key, установленным в 0.

    save_state(self): Сохраняет текущее состояние, добавляя копию объекта в словарь save_obj с ключом, 
    равным self.key, а затем увеличивает self.key на 1.

    recover_state(self, index): Восстанавливает состояние объекта по указанному индексу из save_obj.
    Если индекс не найден, возвращает текущий объект.

    n_states(self): Возвращает количество состояний, хранящихся в объекте, представленное значением self.key.
    """


from copy import deepcopy


class Selfie:
    def __init__(self) -> None:
        self.save_obj = {}
        self.key = 0

    def save_state(self):
        """
        Сохраняет текущее состояние, добавляя копию объекта в словарь `save_obj` с ключом, равным `self.key`.
        Затем увеличивает атрибут `self.key` на 1.
        """
        self.save_obj.setdefault(self.key, deepcopy(self))
        self.key += 1

    def recover_state(self, index):
        """
        Recovers the state of the object at the given index.

        Args:
            index (int): The index of the state to recover.

        Returns:
            Selfie: The recovered state of the object at the given index. If the index is not found, returns the current object.
        """
        try:
            return self.save_obj[index]
        except KeyError:
            return self

    def n_states(self):
        """
        Returns the number of states stored in the object.

        :return: An integer representing the number of states.
        """
        return self.key


# INPUT DATA:

# # TEST_1:
# obj = Selfie()

# obj.x = 1
# obj.y = 2

# print(obj.x)
# print(obj.y)

# obj.save_state()
# obj.x = 0
# obj.y = 0
# print(obj.x)
# print(obj.y)

# obj = obj.recover_state(0)
# print(obj.x)
# print(obj.y)

# # TEST_2:
# obj = Selfie()

# print(obj.n_states())
# obj.x = 0
# obj.save_state()
# obj.x = 1
# obj.save_state()
# obj.x = 2
# obj.save_state()
# print(obj.n_states())

# # TEST_3:
# from string import ascii_lowercase

# obj = Selfie()
# for char in ascii_lowercase:
#     obj.__dict__[char] = ord(char)

# print(*(obj.__dict__[char] for char in ascii_lowercase))
# obj.save_state()

# for char in ascii_lowercase:
#     obj.__dict__[char] = ord(char) + 100

# print(*(obj.__dict__[char] for char in ascii_lowercase))
# obj = obj.recover_state(0)

# print(*(obj.__dict__[char] for char in ascii_lowercase))

# # TEST_4:
# def sum_a_b(a, b):
#     return a + b


# def sub_a_b(a, b):
#     return a - b


# def mul_a_d(a, b):
#     return a * b


# def truediv_a_b(a, b):
#     return a / b


# obj = Selfie()
# obj.sum_a_b = sum_a_b
# print(obj.sum_a_b(1, 2))
# obj.save_state()

# obj.sub_a_b = sub_a_b
# print(obj.sub_a_b(1, 2))
# obj.save_state()

# obj.mul_a_d = mul_a_d
# print(obj.mul_a_d(1, 2))
# obj.save_state()

# obj.truediv_a_b = truediv_a_b
# print(obj.truediv_a_b(1, 2))
# obj.save_state()

# print(obj.n_states())
# obj = obj.recover_state(1)

# print(obj.n_states())

# TEST_5:
obj = Selfie()

obj.x = 1
obj.y = 2

print(obj.x)
print(obj.y)

obj.x = 100
obj.y = 100

obj.save_state()
print(obj.x)
print(obj.y)

obj = obj.recover_state(7)
print(obj.x)
print(obj.y)
