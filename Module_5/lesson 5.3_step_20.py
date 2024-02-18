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
        return tuple(map(int, vers))

    def __str__(self) -> str:
        return ".".join(map(str, self.get_version))

    def __repr__(self) -> str:
        return f"{__class__.__name__}('{'.'.join(map(str, self.get_version))}')"

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, __class__):
            return self.get_version == __value.get_version
        return NotImplemented

    def __ge__(self, __value: object) -> bool:
        if isinstance(__value, __class__):
            return self.get_version >= __value.get_version
        return NotImplemented

# @total_ordering
# class Version:
#     def __init__(self, version):
#         self._parts = [int(i) for i in version.split('.')]
#         self._parts += [0] * (3 - len(self._parts))

#     def __str__(self):
#         return '{}.{}.{}'.format(*self._parts)
    
#     def __repr__(self):
#         return "Version('{}.{}.{}')".format(*self._parts)
    
#     def __eq__(self, other):
#         if isinstance(other, Version):
#             return self._parts == other._parts
#         return NotImplemented
    
#     def __lt__(self, other):
#         if isinstance(other, Version):
#             return self._parts < other._parts
#         return NotImplemented



versions = [Version('162.5'), Version('68.3'), Version('173.8'), Version('108.9'), Version('159.6'), Version('145.7'),
            Version('187.6'), Version('137.7'), Version('33.7'), Version('22.4'), Version('199.4'), Version('122.1'),
            Version('47.4'), Version('10.2'), Version('164.9'), Version('191.6'), Version('139.9'), Version('184.4'),
            Version('94.9'), Version('188.6'), Version('56.8'), Version('138.7'), Version('83.2'), Version('59.4'),
            Version('189.7'), Version('128.5'), Version('6.6'), Version('111.2'), Version('5.6'), Version('188.8'),
            Version('64.9'), Version('76.6'), Version('85.5'), Version('195.6'), Version('12.8'), Version('66.7'),
            Version('121.7'), Version('20.3'), Version('9.8'), Version('140.8'), Version('70.3'), Version('12.3'),
            Version('97.9'), Version('10.4'), Version('98.5'), Version('74.1'), Version('164.8'), Version('55.1'),
            Version('147.7'), Version('39.2'), Version('27.4'), Version('50.3'), Version('174.7'), Version('196.9'),
            Version('106.3'), Version('89.1'), Version('59.9'), Version('189.4'), Version('45.7'), Version('158.2'),
            Version('147.5'), Version('3.2'), Version('49.9'), Version('173.6'), Version('63.9'), Version('8.2'),
            Version('29.4'), Version('15.7'), Version('85.2'), Version('109.2'), Version('152.9'), Version('49.6'),
            Version('53.5'), Version('26.7'), Version('135.9'), Version('155.3'), Version('134.7'), Version('159.4'),
            Version('99.3'), Version('188.9'), Version('197.4'), Version('99.2'), Version('160.5'), Version('183.7'),
            Version('74.2'), Version('184.7'), Version('139.8'), Version('199.2'), Version('122.1'), Version('198.7'),
            Version('190.1'), Version('200.2'), Version('40.3'), Version('150.4'), Version('20.2'), Version('186.7'),
            Version('47.2'), Version('57.5'), Version('72.8'), Version('23.1')]

print(sorted(versions))
print(min(versions))
print(max(versions))

# version = Version('12')
# not_supported = ['12.0.0', 12.0, (12, 0), {12: 0}, True, False]

# for obj in not_supported:
#     print(obj == version)

# TEST_6:
# version = Version('25')

# print(version.__eq__(1))
# print(version.__ne__(1.1))
# print(version.__gt__(range(5)))
# print(version.__lt__([1, 2, 3]))
# print(version.__ge__({4, 5, 6}))
# print(version.__le__({1: 'one'}))

# TEST_7:
# version1 = Version('162')
# version2 = Version('162.0')
# version3 = Version('162.0.0')

# print(version1)
# print(version2)
# print(version3)