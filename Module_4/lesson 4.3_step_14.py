from collections import Counter


class Postman:
    def __init__(self) -> None:
        self.delivery_data = []

    def add_delivery(self, street, home, flat) -> None:
        self.delivery_data.append((street, home, flat))

    def get_houses_for_street(self, street) -> list[str]:
        home = [h for s, h, _ in self.delivery_data if street == s]
        return list(Counter(home).keys())

    def get_flats_for_house(self, street, home) -> list:
        flat = [f for s, h, f in self.delivery_data if street == s and home == h]
        return list(Counter(flat).keys())


postman = Postman()

print(postman.delivery_data)
print(postman.get_houses_for_street("3-я ул. Строителей"))
print(postman.get_flats_for_house("3-я ул. Строителей", 25))
