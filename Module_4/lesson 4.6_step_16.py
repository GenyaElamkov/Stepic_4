class Color:
    def __init__(self, hexcode) -> None:
        # self.hexcode = hexcode
        self.r, self.g, self.b = hexcode[::2]
    
    @property
    def hexcode(self):
        return
    
    @hexcode.setter
    def hexcode(self):
        return