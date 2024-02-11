from functools import singledispatchmethod


class Processor:

    @singledispatchmethod
    @classmethod
    def process(cls, data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @process.register(float)
    @process.register(int)
    @classmethod
    def _int_process(cls, data):
        return data * 2

    @process.register(str)
    @classmethod
    def _str_float_process(cls, data):
        return data.upper()

    @process.register(list)
    @classmethod
    def _list_float_process(cls, data):
        return sorted(data)

    @process.register(tuple)
    @classmethod
    def _tuple_float_process(cls, data):
        return tuple(sorted(data))
