class Const:
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)

    def __getattribute__(self, __name: str):
        return object.__getattribute__(self, __name)

    def __setattr__(self, __name: str, __value):
        if __name in self.__dict__:
            raise AttributeError("Изменение значения атрибута невозможно")
        return object.__setattr__(self, __name, __value)

    def __delattr__(self, __name: str) -> None:
        raise AttributeError("Удаление атрибута невозможно")


videogame = Const(name="Cuphead")

videogame.developer = "Studio MDHR"
print(videogame.name)
print(videogame.developer)

# videogame = Const(name='Disco Elysium')

# try:
#     videogame.name = 'Half-Life: Alyx'
# except AttributeError as e:
#     print(e)


# videogame = Const(name='The Last of Us')

# try:
#     del videogame.name
# except AttributeError as e:
#     print(e)
