# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
user_input = int(input("Введите номер месяца от 1 до 12 "))
my_dict = {'Зима': [12, 1, 2],
           'Весна': [3, 4, 5],
           'Лето': [6, 7, 8],
           'Осень': [9, 10, 11]}
if user_input in my_dict['Зима']:
    print(f"{user_input} месяц относится к зимнему сезону")
elif user_input in my_dict['Весна']:
    print(f"{user_input} месяц относится к весеннему сезону")
elif user_input in my_dict['Лето']:
    print(f"{user_input} месяц относится к летнему сезону")
else:
    print(f"{user_input} месяц относится к осеннему сезону")
