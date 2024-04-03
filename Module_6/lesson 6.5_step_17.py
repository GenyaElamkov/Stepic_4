class HtmlTag:
    __spice = -1

    def __init__(self, tag: str, inline: bool = False) -> None:
        self.tag = tag
        self.inline = inline

    def __enter__(self):
        __class__.__spice += 1
        if not self.inline:
            print(f"{'  ' * __class__.__spice}<{self.tag}>")
        return self

    def __exit__(self, *args) -> None:
        if not self.inline:
            print(f"{'  ' * __class__.__spice}</{self.tag}>")

        __class__.__spice -= 1

    def print(self, text: str) -> None:
        if not self.inline:
            __class__.__spice += 1
            print("  " * __class__.__spice + text)
            __class__.__spice -= 1

        else:
            print(f"{'  ' * __class__.__spice}<{self.tag}>{text}</{self.tag}>")


# class HtmlTag:
#     INDENT = 2
#     depth = 0

#     def __init__(self, tag, inline=False):
#         self.tag = tag
#         self.depth = type(self).depth
#         self.inline = inline
#         self.end_char = '' if inline else '\n'

#     def __enter__(self):
#         print(' ' * type(self).INDENT * self.depth + f'<{self.tag}>', end=self.end_char)
#         type(self).depth += 1
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.inline:
#             print(f'</{self.tag}>')
#         else:
#             print(' ' * type(self).INDENT * self.depth + f'</{self.tag}>')
#         type(self).depth -= 1

#     def print(self, txt):
#         if self.inline:
#             print(txt, end=self.end_char)
#         else:
#             print(' ' * type(self).INDENT * (self.depth + 1) + txt, end=self.end_char)


# INPUT DATA:

# TEST_1:
with HtmlTag("body") as _:
    with HtmlTag("h1") as header:
        header.print("Поколение Python")
    with HtmlTag("p") as section:
        section.print(
            "Cерия курсов по языку программирования Python от команды BEEGEEK"
        )

# TEST_2:
with HtmlTag("body") as _:
    with HtmlTag("h1", True) as header:
        header.print("Поколение Python")
    with HtmlTag("p", True) as section:
        section.print(
            "Cерия курсов по языку программирования Python от команды BEEGEEK"
        )

# # TEST_3:
# with HtmlTag("body") as _:
#     with HtmlTag("h1", True) as header:
#         header.print("Здесь есть что-то интересное")
#     with HtmlTag("a", True) as section:
#         section.print("https://stepik.org/media/attachments/course/98974/watch_me.mp4")

# # TEST_4:
# with HtmlTag("div") as _:
#     with HtmlTag("p") as paragraph:
#         with HtmlTag("strong", True) as strong:
#             strong.print("Notice:")
#         paragraph.print("Your browser is ancient")

# TEST_5:
with HtmlTag("table") as _:
    with HtmlTag("tr") as paragraph:
        with HtmlTag("th", True) as field:
            field.print("текст заголовка")
        with HtmlTag("td") as data:
            with HtmlTag("ul"):
                with HtmlTag("li", True) as marked_list:
                    marked_list.print("данные")
                with HtmlTag("li", True) as marked_list:
                    marked_list.print("данные")
                with HtmlTag("li", True) as marked_list:
                    marked_list.print("данные")
                with HtmlTag("li", True) as marked_list:
                    marked_list.print("данные")
                with HtmlTag("li", True) as marked_list:
                    marked_list.print("данные")
