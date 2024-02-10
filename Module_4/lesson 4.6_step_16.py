class Color:
    def __init__(self, hexcode: str) -> None:
        self.hexcode = hexcode

    @property
    def hexcode(self) -> str:
        return self._hexcode

    @hexcode.setter
    def hexcode(self, hexcode: str) -> None:
        self._hexcode = hexcode
        self.r = int(self._hexcode[:2], 16)
        self.g = int(self._hexcode[2:4], 16)
        self.b = int(self._hexcode[4:], 16)
        

color = Color('0000FF')

print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

# color = Color("0000FF")

# color.hexcode = "A782E3"
# print(color.hexcode)
# print(color.r)
# print(color.g)
# print(color.b)
