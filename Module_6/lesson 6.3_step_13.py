def print_file_content(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            context = file.read()
        print(context)
    except FileNotFoundError:
        print("Файл не найден")


with open("Precepts_of_Zote.txt", "w", encoding="utf-8") as file:
    file.write("Сражения и путешествия берут своё")

print_file_content("Precepts_of_Zote.txt")

print_file_content("Precepts_of_Zote2.txt")
