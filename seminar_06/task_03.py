# list comprehension
# Что сделать с элементом, с каким элементом, при каком условии
input_list = [1, 2, 3, 5, 1, 5, 3, 10]
res = [item for item in input_list if input_list.count(item) == 1]
print(res)


# filter
# При каком условии, элемент
res = list(filter(lambda x: input_list.count(x) == 1, input_list))
print(res)

# map
# Преобразует
input_list = ['423', 'tr', '57', 'aavxc']
res = list(map(lambda x: int(x) if x.isdigit() else x, input_list))
print(res)