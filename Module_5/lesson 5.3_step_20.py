from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version) -> None:
        self.version = version

    @property
    def get_version(self):
        vers = self.version.split(".")
        if len(vers) < 3:
            vers.extend(["0"] * (3 - len(vers)))
        return tuple(vers)

    def __str__(self) -> str:
        return self.version

    def __repr__(self) -> str:
        return f"{__class__.__name__}('{self.version}')"

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, __class__):
            return self.get_version == __value
        return NotImplemented

    def __ge__(self, __value: object) -> bool:
        if isinstance(__value, __class__):
            return self.get_version >= __value
        return NotImplemented


print(Version("3") == Version("3.0"))
print(Version("3") == Version("3.0.0"))
print(Version("3.0") == Version("3.0.0"))
