from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress: str) -> None:
        self.ipaddress = ipaddress

    @__init__.register(tuple)
    @__init__.register(list)
    def _(self, ipaddress):
        self.ipaddress = ".".join(map(str, ipaddress))

    def __str__(self) -> str:
        return self.ipaddress

    def __repr__(self) -> str:
        return f"{__class__.__name__}('{self.ipaddress}')"


ip = IPAddress([1, 1, 10, 10])

print(str(ip))
print(repr(ip))


ip = IPAddress("8.8.1.1")

print(str(ip))
print(repr(ip))
