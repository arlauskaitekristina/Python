# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Мы неабв очень любим Питон иабв Джавабв'
# # 'Мы очень любим Питон'

text = 'Мы неабв очень любим Питон иабв Джавабв'
text_find = 'абв'
index = 0

list = text.split(' ')

print(list)
# i = 0
# while i in range(len(list)):
#     if text_find in list[i]:
#         list.remove(list[i])
#     else:
#         i += 1

list = [item for item in list if text_find not in item]
print(list)