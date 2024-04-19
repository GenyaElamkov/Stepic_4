from datetime import datetime, timedelta


class Lecture:
    def __init__(self, topic: str, start_time: str, duration: str) -> None:
        self.topic = topic
        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.duration = datetime.strptime(duration, "%H:%M")


class Conference:
    """Конференция протяженность в один день."""

    _lectures = []
    _end_time = timedelta(minutes=0.00, hours=0.00)

    def add(self, lecture: Lecture):
        ds = timedelta(minutes=lecture.start_time.minute, hours=lecture.start_time.hour)
        dd = timedelta(minutes=lecture.duration.minute, hours=lecture.duration.hour)

        self._lectures.append(lecture)
        self._lectures.sort(key=lambda date: date.start_time)
        try:
            for i, date in enumerate(self._lectures):
                ds = timedelta(
                    minutes=date.start_time.minute, hours=date.start_time.hour
                )
                dd = timedelta(minutes=date.duration.minute, hours=date.duration.hour)
                ds_next = self._lectures[i + 1].start_time
                ds_next = timedelta(minutes=ds_next.minute, hours=ds_next.hour)
                self._end_time = ds + dd

                if self._end_time > ds_next:
                    raise ValueError("Провести выступление в это время невозможно")
        except IndexError:
            pass

    def _format_date(self, date: timedelta):
        hours, div = divmod(date.total_seconds(), 3600)
        minute = div // 60
        return f"{int(hours):02}:{int(minute):02}"

    def total(self):
        times = timedelta()
        for date in self._lectures:
            dd = timedelta(minutes=date.duration.minute, hours=date.duration.hour)
            times += dd
        return self._format_date(times)

    def longest_lecture(self):
        res = max(self._lectures, key=lambda date: date.duration)
        return res.duration.strftime("%H:%M")

    def longest_break(self):
        try:
            largest = timedelta()
            for i, date in enumerate(self._lectures):
                ds_next = self._lectures[i + 1].start_time
                ds_next = timedelta(minutes=ds_next.minute, hours=ds_next.hour)
                ds = timedelta(
                    minutes=date.start_time.minute, hours=date.start_time.hour
                )
                dd = timedelta(minutes=date.duration.minute, hours=date.duration.hour)
                res = ds_next - (ds + dd)
                if largest < res:
                    largest = res
        except IndexError:
            pass

        return self._format_date(largest)


# from bisect import insort
# from datetime import datetime, timedelta

# from dateutil.relativedelta import relativedelta


# class Lecture:
#     _PATTERN = '%H:%M'

#     def __init__(self, topic, start_time, duration):
#         self.topic = topic
#         self.start_time = datetime.strptime(start_time, self._PATTERN)
#         self.duration = datetime.strptime(duration, self._PATTERN)
#         self.end_time = self.start_time + timedelta(hours=self.duration.hour, minutes=self.duration.minute)


# class Conference:
#     def __init__(self):
#         self.lectures = []

#     def add(self, lecture):
#         for cur_lecture in self.lectures:
#             if any((
#                     cur_lecture.start_time <= lecture.start_time < cur_lecture.end_time,
#                     lecture.start_time <= cur_lecture.start_time < lecture.end_time,
#             )):
#                 raise ValueError('Провести выступление в это время невозможно')
#         insort(self.lectures, lecture, key=lambda item: item.start_time)

#     def total(self):
#         total = sum((lecture.end_time - lecture.start_time for lecture in self.lectures), start=relativedelta())
#         return f'{total.hours:0>2}:{total.minutes:0>2}'

#     def longest_lecture(self):
#         longest = max(lecture.duration for lecture in self.lectures)
#         return f'{longest.hour:0>2}:{longest.minute:0>2}'

#     def longest_break(self):
#         longest = max(self.lectures[i + 1].start_time - self.lectures[i].end_time for i in range(len(self.lectures) - 1))
#         hours, minutes = int(longest.total_seconds()) // 3600, (int(longest.total_seconds()) // 60) % 60
#         return f'{hours:0>2}:{minutes:0>2}'


# INPUT DATA:

# TEST_1:
conference = Conference()

conference.add(Lecture("Простые числа", "08:00", "01:30"))
conference.add(Lecture("Жизнь после ChatGPT", "10:00", "02:00"))
conference.add(Lecture("Муравьиный алгоритм", "13:30", "01:50"))
print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())

# # TEST_2:
# conference = Conference()
# conference.add(Lecture("Простые числа", "08:00", "01:30"))

# try:
#     conference.add(Lecture("Жизнь после ChatGPT", "09:00", "02:00"))
# except ValueError as error:
#     print(error)

# # TEST_3:
# conference = Conference()
# conference.add(Lecture("Простые числа", "08:00", "01:00"))
# conference.add(Lecture("Жизнь после ChatGPT", "11:00", "02:00"))

# try:
#     conference.add(Lecture("Муравьиный алгоритм", "10:00", "04:00"))
# except ValueError as error:
#     print(error)

# # TEST_4:
# conference = Conference()
# conference.add(Lecture("Муравьиный алгоритм", "09:30", "02:00"))
# conference.add(Lecture("Жизнь после ChatGPT", "11:45", "04:00"))
# conference.add(Lecture("Простые числа", "08:00", "01:30"))

# print(conference.longest_lecture())
# print(conference.longest_break())

# # TEST_5:
# conference = Conference()
# conference.add(Lecture("Введение в ООП", "09:30", "00:30"))
# conference.add(Lecture("Атрибуты объектов и классов", "08:00", "01:30"))
# conference.add(Lecture("Методы экземляра класса", "10:30", "02:00"))

# print(conference.longest_lecture())
# print(conference.longest_break())

# # TEST_6:
# conference = Conference()
# conference.add(Lecture("Декоратор @property", "09:30", "00:30"))
# conference.add(Lecture("Свойства", "09:00", "00:30"))
# conference.add(Lecture("Модификаторы доступа и аксессоры", "08:30", "00:30"))

# print(conference.longest_lecture())
# print(conference.longest_break())

# # TEST_7:
# conference = Conference()
# conference.add(Lecture("Декораторы @classmethod и @staticmethod", "09:30", "00:30"))

# try:
#     conference.add(Lecture("Декоратор @singledispatchmethod", "09:30", "00:30"))
# except ValueError as e:
#     print(e)

# # TEST_8:
# conference = Conference()
# conference.add(Lecture("Декораторы @classmethod и @staticmethod", "09:30", "00:30"))

# try:
#     conference.add(Lecture("Декоратор @singledispatchmethod", "09:45", "00:30"))
# except ValueError as e:
#     print(e)

# # TEST_9:
# conference = Conference()
# conference.add(Lecture("Декораторы @classmethod и @staticmethod", "09:30", "00:30"))

# try:
#     conference.add(Lecture("Декоратор @singledispatchmethod", "09:59", "00:30"))
# except ValueError as e:
#     print(e)

# # TEST_10:
# conference = Conference()
# conference.add(Lecture("Декораторы @classmethod и @staticmethod", "09:30", "00:30"))

# try:
#     conference.add(Lecture("Декоратор @singledispatchmethod", "09:00", "00:35"))
# except ValueError as e:
#     print(e)

# # TEST_11:
# conference = Conference()
# conference.add(Lecture("Декораторы @classmethod и @staticmethod", "09:30", "00:30"))
# conference.add(Lecture("Декоратор @singledispatchmethod", "09:00", "00:30"))
# conference.add(Lecture("Создание, инициализация и очищение объектов", "11:00", "00:30"))

# start_times = [
#     "09:30",
#     "09:45",
#     "09:59",
#     "09:00",
#     "09:00",
#     "09:15",
#     "09:29",
#     "08:30",
#     "11:00",
#     "11:15",
#     "11:25",
#     "10:45",
# ]
# durations = [
#     "00:30",
#     "00:30",
#     "00:30",
#     "00:35",
#     "00:15",
#     "00:15",
#     "00:30",
#     "00:35",
#     "00:20",
#     "00:10",
#     "00:35",
#     "00:16",
# ]

# for start_time, duration in zip(start_times, durations):
#     try:
#         conference.add(
#             Lecture("Строковое представление объектов", start_time, duration)
#         )
#     except ValueError as e:
#         print(e)

# # TEST_12:
# conference = Conference()
# conference.add(Lecture("Декораторы @classmethod и @staticmethod", "09:30", "00:30"))
# conference.add(Lecture("Декоратор @singledispatchmethod", "09:00", "00:30"))
# conference.add(Lecture("Создание, инициализация и очищение объектов", "11:00", "00:30"))
# conference.add(Lecture("Унарные операторы и функции", "10:45", "00:15"))
# conference.add(Lecture("Арифметические операции", "10:00", "00:30"))
# conference.add(Lecture("Вызываемые объекты", "08:00", "01:00"))

# print(conference.total())
# print(conference.longest_lecture())
# print(conference.longest_break())
