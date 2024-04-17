def get_method_owner(cls, method):
    for elem in cls.mro():
        if method in elem.__dict__:
            return elem


class A:
    pass
        
class B(A):
    pass

print(get_method_owner(B, 'm'))