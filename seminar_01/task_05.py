# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно (5 и 10) или (15, но не 30

# num = int(input("Введите число: "))
# if ((num % 5 == 0) and (num % 10 == 0)) or ((num % 15 == 0) and (num % 30 != 0)):
#     print("Да")
# else:
#     print("Нет")

num=int(input("Введите число: "))
if (num % 5 == 0) and (num % 10 == 0):
    print ("число ", num, "кратно 5 и 10")
if (num % 15 == 0) and (num % 30 != 0):
    print (f"число ", num, "кратно 15, но не кратно 30")