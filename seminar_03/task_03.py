#  Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# myList = ["1", "qwe", "asd", "zxc", "qwe", "ertqwe", "qwe"]
# myString = 'qwe'
# count = 0

# for i in range(0, len(myList)):
#     if myList[i] == myString:
#         count += 1
#         if count == 2:
#             print(i)
#             break
# if count < 2:
#     print("False")

list = ["qwe", "asd", "zxc", "qwe", "ertqwe", "asd", "asd"]
y = input('Input string ')
count = 0
for i in range(len(list)):
    if list[i] == y:
        count += 1
        if count == 2:
            print(i)