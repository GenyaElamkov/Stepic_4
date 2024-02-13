class PhoneNumber:
    def __init__(self, phone_number: str) -> None:
        self.phone_number = phone_number.replace(" ", "")

    def __str__(self) -> str:
        return (
            f"({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}"
        )

    def __repr__(self) -> str:
        return f"{__class__.__name__}('{self.phone_number}')"


phone = PhoneNumber("9173963385")

print(str(phone))
print(repr(phone))

phone = PhoneNumber("918 396 3389")

print(str(phone))
print(repr(phone))
