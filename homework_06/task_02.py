# Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['65h34q', 'sdg634d', '147jnbv']
# "7"

myList = ['65h34q', 'sdg634d', '147jnbv']
num = '5'

res = [i for i in myList if i.find(num) >= 0]
print(res)

