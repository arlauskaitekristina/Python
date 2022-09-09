# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

element = int(input('Введите число N: '))
num = list(range(-element, element+1))
print("Заданный список", num)

print("Введите через пробел индексы чисел от 0 до", num.index(element))
one, two = map(int, input().split())
for i in range (len(num)):
    mult = num[one] * num[two]
print('Произведение элементов на заданных позициях =', mult)
