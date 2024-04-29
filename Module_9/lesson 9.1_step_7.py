class Pagination:
    def __init__(self, alphabet: list, sizen) -> None:
        self.alphabet = self._chuncks(alphabet, sizen)
        self.sizen = sizen
        self.total_pages = len(self.alphabet)
        self.current_page = 1

    def _chuncks(self, alphabet, sizen):
        return [alphabet[i : i + sizen] for i in range(0, len(alphabet), sizen)]

    def _check_list(self, num_page):
        if num_page <= 0:
            self.first_page()
        if num_page > self.total_pages:
            self.last_page()

    def get_visible_items(self):
        return self.alphabet[self.current_page - 1]

    def prev_page(self):
        self.current_page -= 1
        self._check_list(self.current_page)
        return self

    def next_page(self):
        self.current_page += 1
        self._check_list(self.current_page)
        return self

    def first_page(self):
        self.current_page = 1

    def last_page(self):
        self.current_page = self.total_pages

    def go_to_page(self, num_page):
        self.current_page = num_page
        self._check_list(num_page)


# INPUT DATA:

# # TEST_1:
# alphabet = list('abcdefghijklmnopqrstuvwxyz')

# pagination = Pagination(alphabet, 4)
# print(pagination.get_visible_items())


# # TEST_2:
# alphabet = list("abcdefghijklmnopqrstuvwxyz")

# pagination = Pagination(alphabet, 4)
# pagination.next_page()
# print(pagination.get_visible_items())

# pagination.last_page()
# print(pagination.get_visible_items())

# # TEST_3:
# alphabet = list('abcdefghijklmnopqrstuvwxyz')

# pagination = Pagination(alphabet, 4)
# pagination.next_page().next_page()
# print(pagination.get_visible_items())
# print(pagination.total_pages)
# print(pagination.current_page)

# # TEST_4:
# alphabet = list('abcdefghijklmnopqrstuvwxyz')

# pagination = Pagination(alphabet, 4)
# pagination.prev_page()
# print(pagination.get_visible_items())

# pagination.last_page()
# pagination.next_page()
# print(pagination.get_visible_items())

# # TEST_5:
# alphabet = list('abcdefghijklmnopqrstuvwxyz')

# pagination = Pagination(alphabet, 4)
# pagination.go_to_page(-100)
# print(pagination.get_visible_items())

# pagination.go_to_page(100)
# print(pagination.get_visible_items())

# # TEST_6:
# text = '''У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо — песнь заводит,
# Налево — сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кощей над златом чахнет;
# Там русский дух… там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.'''.splitlines()

# pagination = Pagination(text, 5)
# print(pagination.get_visible_items())

# # TEST_7:
# text = '''У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо — песнь заводит,
# Налево — сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кощей над златом чахнет;
# Там русский дух… там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.'''.splitlines()

# pagination = Pagination(text, 5)
# pagination.next_page()
# print(pagination.get_visible_items())

# pagination.last_page()
# print(pagination.get_visible_items())

# pagination.first_page()
# print(pagination.get_visible_items())

# # TEST_8:
# text = '''У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо — песнь заводит,
# Налево — сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кощей над златом чахнет;
# Там русский дух… там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.'''.splitlines()

# pagination = Pagination(text, 5)
# pagination.next_page().next_page()
# print(pagination.get_visible_items())
# print(pagination.total_pages)
# print(pagination.current_page)

# # TEST_9:
# text = '''У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо — песнь заводит,
# Налево — сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кощей над златом чахнет;
# Там русский дух… там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.'''.splitlines()

# pagination = Pagination(text, 5)
# pagination.prev_page()
# print(pagination.get_visible_items())

# pagination.last_page()
# pagination.next_page()
# print(pagination.get_visible_items())

# # TEST_10:
# text = '''У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо — песнь заводит,
# Налево — сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кощей над златом чахнет;
# Там русский дух… там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.'''.splitlines()

# pagination = Pagination(text, 5)
# pagination.go_to_page(-100)
# print(pagination.get_visible_items())

# pagination.go_to_page(100)
# print(pagination.get_visible_items())

# # TEST_11:
# text = '''У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо — песнь заводит,
# Налево — сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кощей над златом чахнет;
# Там русский дух… там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.'''.splitlines()

# pagination = Pagination(text, 5)

# pagination.last_page()
# pagination.prev_page().prev_page()
# print(pagination.get_visible_items())

# # TEST_12:
# alphabet = list('abcd')

# pagination = Pagination(alphabet, 4)
# pagination.next_page()
# print(pagination.get_visible_items())

# TEST_13:
alphabet = list("abcdefghijklmnopqrstuvwxyz")
pagination = Pagination(alphabet, 4)
pages = [7, 3, 6, 1, 4, 2, 5]

for page in pages:
    pagination.go_to_page(page)
    print(pagination.get_visible_items())
