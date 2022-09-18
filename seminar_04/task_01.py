# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

from tkinter import N


ourstr = input('Enter your strings via space: '). split(' ')

def list_add(ourstr):
    numbers = []
    for i in range(len(ourstr)):
        numbers.append(int(ourstr[i]))
    return numbers

numbers = list_add(ourstr)
print(numbers)
print(f'Your min value is: {min(numbers)};\nYour max value is: {max(numbers)}')