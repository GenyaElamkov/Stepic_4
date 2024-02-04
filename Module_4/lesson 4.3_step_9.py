class Scales:
    def __init__(self) -> None:
        self.cup_right = 0
        self.cup_left = 0

    def add_right(self, massa):
        self.cup_right += massa

    def add_left(self, massa):
        self.cup_left += massa

    def get_result(self):
        if self.cup_right > self.cup_left:
            return "Правая чаша тяжелее"
        if self.cup_right < self.cup_left:
            return "Левая чаша тяжелее"
        return "Весы в равновесии"

scales = Scales()

scales.add_right(1)
scales.add_right(1)
scales.add_left(2)

print(scales.get_result())
