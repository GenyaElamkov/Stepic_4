class H: ...


class D(H): ...


class E(H): ...


class F(H): ...


class G(H): ...


class C(F, G): ...


class B(D, E): ...


class A(B, C): ...


# INPUT DATA:

# TEST_1:
print(issubclass(D, H))
print(issubclass(E, H))
print(issubclass(F, H))
print(issubclass(G, H))

# TEST_2:
print(issubclass(B, D))
print(issubclass(B, E))
print(issubclass(B, F))
print(issubclass(B, G))

# TEST_3:
print(issubclass(C, D))
print(issubclass(C, E))
print(issubclass(C, F))
print(issubclass(C, G))

# TEST_4:
print(A.mro())

# TEST_5:
print(issubclass(A, H))
print(issubclass(B, H))
print(issubclass(C, H))