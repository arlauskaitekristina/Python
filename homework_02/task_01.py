# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 0,56 -> 11

num = int(input('Введите вещественное число для получения суммы цифр в этом числе = '))
sum = 0
for elem in num:
    if elem != '.':
        sum += int(elem)
print("Сумма цифр заданного числа = ", sum) 
