class SuperString:
    def __init__(self, string) -> None:
        self.string = string

    def __str__(self) -> str:
        return self.string

    def __add__(self, object):
        if isinstance(object, __class__):
            return __class__(self.string + object.string)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, int):
            return __class__(self.string * n)
        return NotImplemented

    def __rmul__(self, n):
        if isinstance(n, int):
            return self.string.__mul__(n)
        return NotImplemented

    def __truediv__(self, n):
        if isinstance(n, int):
            return __class__(self.string[: len(self.string) // n])
        return NotImplemented

    def __lshift__(self, n):
        if not isinstance(n, int):
            return NotImplemented

        new_instance = __class__(self.string)
        if n < len(self.string):
            return __class__(self.string[: len(self.string) - n])

        if n >= len(self.string):
            new_instance.string = ""
            return __class__(new_instance.string)

    def __rshift__(self, n):
        if not isinstance(n, int):
            return NotImplemented

        new_instance = __class__(self.string)
        if n < len(self.string):
            return __class__(self.string[n:])

        if n >= len(self.string):
            new_instance.string = ""
            return __class__(new_instance.string)


names = ['Карп', 'Фотий', 'Любосмысл', 'Клавдия', 'Милован', 'Светлана', 'Александра', 'Ираида', 'Трифон', 'Добромысл',
         'Евпраксия', 'Радим', 'Эдуард', 'Аристарх', 'Ульяна', 'Ираклий', 'Юлия', 'Марк', 'Демид', 'Творимир', 'Орест',
         'Феоктист', 'Тимур', 'Филипп', 'Аверьян', 'Эраст', 'Осип', 'Станислав', 'Адриан', 'Милан', 'Парфен', 'Велимир',
         'Филимон', 'Ратибор', 'Элеонора', 'Феофан', 'Ирина', 'Кузьма', 'Панфил', 'Венедикт', 'Парамон', 'Влас',
         'Надежда', 'Фрол', 'Мартьян', 'Моисей', 'Леонид', 'Мариан', 'Марина', 'Филарет', 'Валентина', 'Севастьян',
         'Светозар', 'Родион', 'Ростислав', 'Капитон', 'Герман', 'Геннадий', 'Иосиф', 'Гостомысл', 'Епифан', 'Гордей',
         'Ферапонт', 'Януарий', 'Денис', 'Галина', 'Аггей', 'Харлампий', 'Акулина', 'Климент', 'Автоном', 'Никанор',
         'Фортунат', 'Сила', 'Федосий', 'Виктор', 'Арсений', 'Дементий', 'Спартак', 'Евгений', 'Феликс', 'Ананий',
         'Нинель', 'Стоян', 'Остромир', 'Никифор', 'Клавдий', 'Чеслав', 'Афанасий', 'Наум', 'Рубен', 'Азарий',
         'Виктория', 'Синклитикия', 'Тимофей', 'Фёкла', 'Нонна', 'Ким', 'София']

for name in names:
    person = SuperString(name)
    print(person * 2, 2 * person, person / 2)