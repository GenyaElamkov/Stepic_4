class AttrsNumberObject:
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
        self.attrs_num = 0

    def __getattribute__(self, __name: str):
        if __name == "attrs_num":
            return len(self.__dict__)
        return object.__getattribute__(self, __name)

    # def __getattr__(self, __name):
    #     return len(self.__dict__) + 1


# music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')

# print(music_group.attrs_num)

# music_group = AttrsNumberObject()

# print(music_group.attrs_num)

music_group = AttrsNumberObject(name="Woodkid", genre="pop")

print(music_group.attrs_num)
music_group.country = "France"
print(music_group.attrs_num)
