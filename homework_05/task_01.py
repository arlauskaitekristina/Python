# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


text = 'Мы неабв очень любим Питон иабв Джавабв'
text_find = 'абв'
index = 0

list = text.split(' ')

print(list)

list = [item for item in list if text_find not in item]
print(list)