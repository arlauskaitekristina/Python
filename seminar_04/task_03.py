# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Ответ записать в файл.

# a = 13
# b = 2

# count = a * b
# while (a != b):
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# print(count/b)

import math

num_1 = int(input('Enter number: '))
num_2 = int(input('Enter number: '))

print(math.lcm(num_1, num_2))

with open('file.txt', 'a') as f:
    f.write(str(math.lcm(num_1, num_2)))