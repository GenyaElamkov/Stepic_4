# class TitledText(str):
#     def __new__(cls, content, text_title):
#         return super().__new__(cls, content)

#     def __init__(self, content, text_title) -> None:
#         # super().__init__()
#         # Текст
#         self.content = content
#         # Заголовок текста
#         self.text_title = text_title

#     def title(self):
#         return self.text_title


class TitledText(str):
    def __new__(cls, content, text_title, *args, **kwargs):
        instance = super().__new__(cls, content)
        instance._text_title = text_title
        return instance

    def title(self) -> str:
        return self._text_title

# INPUT DATA:

# TEST_1:
titled = TitledText("Сreate a class Soda", "Homework")

print(titled)
print(titled.__dict__)
print(titled.title())
print(issubclass(TitledText, str))

# TEST_2:
titled1 = TitledText("Сreate a class Soda", "Homework")
titled2 = TitledText("Сreate a class Soda", "Exam")

print(titled1 == titled2)

# TEST_3:
headlines = [
    "Как полностью изменить...",
    "Где найти …",
    "Быстрый способ...",
    "Ошибки, которые приведут тебя к ...",
    "Как быстро...",
]
contents = [
    "Нужно всего лишь...",
    "Обратитесь к нам, и мы всё расскажем",
    "Для этого Вы должны",
    "Не делай их",
    "Ну это вообще просто",
]

for heading, content in zip(headlines, contents):
    titledtext = TitledText(content, heading)
    print(titledtext.title(), titledtext)
