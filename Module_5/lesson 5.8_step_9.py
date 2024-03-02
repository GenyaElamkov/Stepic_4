class Logger:
    def __setattr__(self, name, value):
        print(f"Изменение значения атрибута {name} на {value}")
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        print(f"Удаление атрибута {name}")
        object.__delattr__(self, name)


obj = Logger()

obj.attr = 1
del obj.attr


obj = Logger()

obj.name = "pygen"
obj.rating = "5*"
obj.ceo = "Timur"
del obj.rating
obj.rating = "6*"
