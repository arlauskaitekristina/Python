# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите степень: '))
a = int(random.randint(0,100))
b = int(random.randint(0,100))
c = int(random.randint(0,100))
print(f"Случайный список коэффициэнтов многочленов: [{a}, {b}, {c}]")


if a != 0:
    first = (str(a) + "x^" + str(k) + " + ")
else:
    first = (str())

if b != 0:
    second = (str(b) + "x" + " + ")
else:
    second = (str())

if c != 0:
    third = (str(c) + " = 0")
else:
    third = (str())

print('Результат записан в файл task4.txt')

with open('task4.txt', 'a') as f:
    f.write(f'{first}{second}{third}')

