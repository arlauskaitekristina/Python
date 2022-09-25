# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 4 5

with open('Exercise_01.txt', 'r') as f:
    string = f.readline()

string = string.split(' ')
string = list(map(int, string))

for i in range(1, len(string)):
    if string[i] - 1 != string[i - 1]:
        print(f'Missed: {string[i] - 1}')
        break
else:
    print('Goog')
