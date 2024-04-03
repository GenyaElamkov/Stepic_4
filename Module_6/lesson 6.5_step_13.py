from copy import deepcopy


class Atomic:
    def __init__(self, data: list | set | dict, deep: bool = False) -> None:
        self.data = data
        self.deep = deep

    def __enter__(self) -> set | list | dict:
        if not self.deep:
            if isinstance(self.data, set):
                self.__old_data = set(self.data)
            elif isinstance(self.data, dict):
                self.__old_data = {k: v for k, v in self.data.items()}
            else:
                self.__old_data = self.data[:]
        else:
            self.__old_data = deepcopy(self.data)
        return self.__old_data

    def __exit__(self, exc_type, exc_value, traceback) -> True:

        if exc_type is None:
            if isinstance(self.data, set):
                {self.data.add(elem) for elem in self.__old_data}
            elif isinstance(self.data, dict):
                self.data.update(self.__old_data)
            else:
                self.data[:] = self.__old_data

        return True

import copy


class Atomic:
    def __init__(self, data, deep=False):
        self.original = data
        self.copy = copy.deepcopy if deep else copy.copy
        
        if isinstance(data, list):
            self.original_update = self.original.extend
        elif isinstance(data, (set, dict)):
            self.original_update = self.original.update

    def __enter__(self):
        self.data = self.copy(self.original)
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.original.clear()
            self.original_update(self.data)
        return True



# INPUT DATA:

# TEST_1:
numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[1]

print(numbers)

# TEST_2:
numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[100]  # обращение по несуществующему индексу

print(numbers)

# TEST_3:
matrix = [[1, 2], [3, 4]]

with Atomic(matrix) as atomic:
    atomic[1].append(0)  # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]  # обращение по несуществующему индексу

print(matrix)

# TEST_4:
matrix = [[1, 2], [3, 4]]

with Atomic(matrix, True) as atomic:
    atomic[1].append(0)  # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]  # обращение по несуществующему индексу

print(matrix)

# TEST_5:
numbers = {1, 2, 3, 4, 5}

with Atomic(numbers) as atomic:
    atomic.add(6)
    atomic.append(7)  # добавление элемента с помощью несуществующего метода

print(sorted(numbers))

with Atomic(numbers) as atomic:
    atomic.add(6)

print(sorted(numbers))

# TEST_6:
data = {
    "firstname": "Alyson",
    "lastname": "Hannigan",
    "birthday": {"day": 24, "month": "March", "year": 1974},
}

with Atomic(data, True) as atomic:  # deep = True
    atomic["birthday"]["month"] = "April"  # изменение вложенной структуры
    print(atomic["name"])  # обращение по несуществующему ключу

print(data)

with Atomic(data) as atomic:  # deep = False
    atomic["birthday"]["month"] = "April"  # изменение вложенной структуры
    print(atomic["name"])  # обращение по несуществующему ключу

print(data)

# TEST_7:
data = {
    "a": 100,
    "z": 333,
    "b": 200,
    "c": 300,
    "d": 45,
    "e": 98,
    "t": 76,
    "q": 34,
    "f": 90,
    "m": 230,
}

with Atomic(data) as atomic:
    atomic["e"] += 2  # изменение структуры

print(data)

# TEST_8:
matrix = [[1, 2], [3, 4]]

with Atomic(matrix, True) as atomic:
    atomic[1].append(0)

print(matrix)
