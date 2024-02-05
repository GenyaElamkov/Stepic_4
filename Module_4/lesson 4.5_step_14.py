class HourClock:
    def __init__(self, hours: int) -> None:
        self.hours = hours

    def get_hours(self) -> int:
        return self._hours
    
    def set_hours(self, hours: int) -> int:
        if not isinstance(hours, int) or not (0 < hours <= 12):
            raise ValueError("Некорректное время")
        self._hours = hours

    hours = property(get_hours, set_hours)


time = HourClock(7)

print(time.hours)
time.hours = 9
print(time.hours)