from functools import total_ordering

@total_ordering
class RomanNumeral:
    def __init__(self, number) -> None:
        self.number = number

    def __str__(self) -> str:
        return f"{self.number}"
    
    def __int__(self):
        pass

    def __eq__(self, __value: object) -> bool:
        pass

    def __le__(self, __value: object) -> bool:
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass
        
number = RomanNumeral('IV') + RomanNumeral('VIII')

print(number)
print(int(number))