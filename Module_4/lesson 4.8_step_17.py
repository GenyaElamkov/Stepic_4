from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @neg.register(float)
    @neg.register(int)
    @staticmethod
    def _num_neg(data):
        return -1 * data

    @neg.register(bool)
    @staticmethod
    def _bool_neg(data):
        return (True, False)[data]
    

print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))

try:
    Negator.neg('number')
except TypeError as e:
    print(e)