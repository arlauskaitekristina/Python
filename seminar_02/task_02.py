#  Для натурального n создать последовательности 3n + 1.

# *Пример:*
# - Для n = 6:
# 1: 4,
# 2: 7,
# 3: 10,
# 4: 13,
# 5: 16,
# 6: 19

# number = int(input('Enter your number: '))

# for i in range(1, number +1):
#     num = (3 * i + 1)
#     print(f"{i} : {num}")

number = int(input('Введите число: '))

def number (n):
    i = 1
    while i <= n:
        result = 3 * i + 1
        print (f'{i} : {result}')
        i += 1
