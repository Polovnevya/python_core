# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
seconds = int(input("Введите время в секундах "))
hour = int(seconds // 3600)
minutes = int((seconds % 3600) // 60)
seconds = int((seconds % 3600) % 60)
time = f"{hour:02d}:{minutes:02d}:{seconds:02d}"
print(f"Вы ввели {time}")
