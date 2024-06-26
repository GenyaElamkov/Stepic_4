class MROHelper:
    @staticmethod
    def len(cls):
        return len(cls.__mro__)

    @staticmethod
    def class_by_index(cls, n: int = 0):
        return cls.__mro__[n]

    @staticmethod
    def index_by_class(child, parent):
        return child.__mro__.index(parent)


# INPUT DATA:


# TEST_1:
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(MROHelper.len(D))


# TEST_2:
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(MROHelper.class_by_index(D, 2))
print(MROHelper.class_by_index(B))


# TEST_3:
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(MROHelper.index_by_class(D, A))


# TEST_4:
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(A):
    pass


class E(B, C, D):
    pass


class F(B, C):
    pass


print(MROHelper.len(E))
print(MROHelper.class_by_index(E, 4))
print(MROHelper.index_by_class(E, C))
