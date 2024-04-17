class A: ...


class C(A): ...


class B(A): ...


class D(A): ...


class E(B, D): ...


# INPUT DATA:

# TEST_1:
print(issubclass(E, B))
print(issubclass(E, C))
print(issubclass(E, D))

# TEST_2:
print(issubclass(B, A))
print(issubclass(C, A))
print(issubclass(D, A))

# TEST_3:
print(E.mro())

# TEST_4:
print(issubclass(E, A))
