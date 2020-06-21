# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
#   то новый элемент с тем же значением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]
print(f"Текущий рейтинг {my_list}")
print("Введите новое значение рейтинга и нажмите Enter, для окончания ввода нажмите Enter при пустой строке")
while True:
    user_input = int(input("Введите новый рейтинг "))
    if user_input:
        for index, el in enumerate(my_list):
            if int(el) < user_input:
                my_list.insert(index, str(user_input))
                print(f"Элемент рейтинга добавлен в позицию {index+1}")
                break
            elif user_input <= my_list[-1]:
                my_list.insert(len(my_list), str(user_input))
                print(f"Элемент рейтинга добавлен в позицию {len(my_list)}")
                break
        print(f"Текущий рейтинг {my_list}")
    else:
        break
