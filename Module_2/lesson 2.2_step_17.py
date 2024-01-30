"""
Функция pluck()
Реализуйте функцию pluck(), которая принимает три аргумента в следующем порядке:

data — словарь произвольной вложенности
path — строка, представляющая собой ключ или последовательность ключей, перечисленных через точку .
default — произвольный объект, значение по умолчанию; имеет значение None, если не передан явно
Функция должна возвращать значение по ключу path из словаря data. Если path представляет собой последовательность ключей, например, key1.key2, то возвращаемым значением функции должно быть значение по ключу key2 из словаря data[key1]. Если указанного ключа или хотя бы одного ключа из последовательности ключей в словаре нет, функция должна вернуть значение default.

https://stepik.org/lesson/794484/step/17?unit=797232
"""


def testing_lesson(filename: str):
    '''Функция выполняет код из каждого файла и выводит результат выполнения вашего кода и ожидаемый результат'''
    from zipfile import ZipFile

    with ZipFile(filename) as z:
        length = len(z.namelist()) // 2
        files = [(code, out) for code, out in zip(z.namelist()[::2], z.namelist()[1::2])]
        for file_exec, file_out in files:
            with z.open(name=file_exec) as fi:
                with z.open(name=file_out) as fo:
                    code, out = fi.read().decode(), fo.read().decode()
                    ##################################
                    # Тут написанный код из задания. #
                    ##################################
                    def pluck(data: dict, path: str, default="None"):
                        if path in data:
                            return data[path]

                        path = path.split(".")
                        for _ in data:
                            try:
                                if isinstance(data[path[0]], dict):
                                    data = data[path[0]]
                                    del path[0]
                                    return pluck(data, ".".join(path), default)
                            except KeyError:
                                return default
                    ###################################
                    print(f'Тест № {file_exec} из {length}')
                    print(f'\nКод: \n\n{code}\n')
                    print('-' * 100)
                    print('Ваш результат:')
                    try:
                        exec(code)
                        print(f"{'-' * 100}\nОжидаемый результат:\n{out}\n{'*' * 100}")
                    except Exception as e:
                        print(f'{"🚫" * 50}\n"Тест № {file_exec} завершился с `ошибкой "{type(e).__name__}: {e}\n')
                        print(f'Ожидаемый результат: \n{out}\n{"🚫" * 50}"\n')


filename = 'Module_2/lesson 2.2_step_17.zip'
testing_lesson(filename)

# if __name__ == "__main__":
#     d = {"a": {"b": 5, "z": 20}, "c": {"d": 3}, "x": 40}
#     print(pluck(d, "x"))

#     d = {"a": {"b": 5, "z": 20}, "c": {"d": 3}, "x": 40}
#     print(pluck(d, "a.b"))

#     d = {"a": {"b": {"c": {"d": {"e": 4}}}}}
#     print(pluck(d, "a.b.c"))

#     d = {"a": {"b": 5, "z": 20}, "c": {"d": 3}, "x": 40}
#     print(pluck(d, "c.d"))

#     d = {"a": {"b": 5, "z": 20}, "c": {"d": 3}, "x": 40}
#     print(pluck(d, "c.e"))

#     d = {
#         "firstname": "Тимур",
#         "lastname": "Гуев",
#         "birthdate": {"day": 10, "month": "October", "year": 1993},
#         "address": {
#             "streetaddress": "Часовая 25, кв. 127",
#             "city": {
#                 "region": "Московская область",
#                 "type": "город",
#                 "cityname": "Москва",
#             },
#             "postalcode": "125315",
#         },
#     }
#     print(pluck(d, "birthdate.weekday", default="Not found"))
