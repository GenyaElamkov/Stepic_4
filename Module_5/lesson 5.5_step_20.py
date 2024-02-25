class Time:
    def __init__(self, hours, minutes) -> None:
        self.hours = hours % 24 + minutes // 60
        self.minutes = minutes % 60

    def __str__(self) -> str:
        return f"{self.hours:0>2}:{self.minutes:0>2}"

    def __add__(self, other):
        if isinstance(other, __class__):
            return __class__(self.hours + other.hours, self.minutes + other.minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, __class__):
            self.hours = (self.hours + other.hours) % 24 + (
                self.minutes + other.minutes
            ) // 60
            self.minutes = (self.minutes + other.minutes) % 60

            return self
        return NotImplemented

    def format_time(self, hours, minutes):
        self.hours = hours % 24 + minutes // 60
        print(self.hours)
        return self.hours


t = Time(22, 0)
t += Time(3, 0)
print(t)

t1 = Time(15, 50)
t2 = Time(2, 20)
print(t1 + t2)

t1 += Time(2, 20)
print(t1)
