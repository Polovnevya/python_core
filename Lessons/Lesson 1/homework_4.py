# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number = int(input("Введите целое положительное число "))
max_digit = 0
digit_counter = number
while digit_counter:
    if max_digit == 9:
        break
    elif max_digit <= (digit_counter % 10):
        max_digit = digit_counter % 10
    digit_counter = digit_counter // 10
print(f"Самой большой цифрой в числе {number} является {max_digit}")
