# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]


numbers = list(map(int,input('Введите числа списка через пробел: ').split()))
new_lst = []
[new_lst.append(i) for i in numbers if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")