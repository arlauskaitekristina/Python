import sys
def initial_phonebook():
    temp = []
    print('Чтобы начать предлагаем сохранить первый контакт...\n')
    phone_book = []
    rows = 1
    cols = 4
    for i in range(rows): 
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Введите фамилию: ")))
            if j == 1:
                temp.append(str(input("Введите имя: ")))
            if j == 2:
                temp.append(str(input("Введите номер телефона: ")))
            if j == 3:
                temp.append(str(input("Введите категорию (Семья/Друзья/Работа/Другие): ")))
    phone_book.append(temp)
    print('\nНомер телефона добавлен!')
    with open(r'C:\Users\New\Desktop\VS_Code\python_seminar\homework_07_pb\Phonebook\phoneb.csv', 'a+', encoding='utf-8') as file:
        file.write(f"\n{temp[0]}\n{temp[1]}\n{temp[2]}\n{temp[3]}\n{temp[0]}, {temp[1]}, {temp[2]}, {temp[3]}")
    return phone_book
