# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
user_input = input("Введите строку из нескольких слов, разделённых пробелами ")
print()
my_list = user_input.split()
for index, word in enumerate(my_list, 1):
    print(f"№ {index} {word.title()[:10]}")
