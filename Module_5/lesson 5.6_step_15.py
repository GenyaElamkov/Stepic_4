from datetime import datetime, date


class DateFormatter:
    __pattern = {
        "ru": "%d.%m.%Y",
        "us": "%m-%d-%Y",
        "ca": "%Y-%m-%d",
        "br": "%d/%m/%Y",
        "fr": "%d.%m.%Y",
        "pt": "%d-%m-%Y",
    }

    def __init__(self, country_code) -> None:
        self.country_code = country_code

    def __call__(self, d: datetime):
        return d.strftime(self.__pattern[self.country_code])


ru_format = DateFormatter("ru")

print(ru_format(date(2022, 11, 7)))


us_format = DateFormatter("us")

print(us_format(date(2022, 11, 7)))
