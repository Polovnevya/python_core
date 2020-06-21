# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
digit = input("Введите число ")
summ = int(digit) + int(digit * 2) + int(digit * 3)
print(f"Сумма чисел {digit} + {digit * 2} + {digit * 3} = {summ}")
