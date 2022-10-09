import json
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
    with open(r'C:\Users\New\Desktop\VS_Code\python_seminar\homework_07_pb\phonebook\pb.csv', 'a+', encoding='utf-8') as file:
        file.write(f"\n{temp[0]}\n{temp[1]}\n{temp[2]}\n{temp[3]}\n{temp[0]}, {temp[1]}, {temp[2]}, {temp[3]}")
    
    with open(r'C:\Users\New\Desktop\VS_Code\python_seminar\homework_07_pb\phonebook\phone_book.json', 'w', encoding='utf-8') as f:
        json.dump(phone_book, f)
    
    return phone_book

def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("\nВведите фамилию: ")))
        if i == 1:
            dip.append(str(input("Введите имя: ")))
        if i == 2:
            dip.append(str(input("Введите номер телефона: ")))
        if i == 3:
            dip.append(str(input("Введите категорию (Семья/Друзья/Работа/Другие): ")))
    print('\nНомер телефона добавлен!')
    
    pb.append(dip)
    with open(r'C:\Users\New\Desktop\VS_Code\python_seminar\homework_07_pb\phonebook\pb.csv', 'a+', encoding='utf-8') as file:
        file.write(f"\n{dip[0]}\n{dip[1]}\n{dip[2]}\n{dip[3]}\n{dip[0]}, {dip[1]}, {dip[2]}, {dip[3]}")
    with open(r'C:\Users\New\Desktop\VS_Code\python_seminar\homework_07_pb\phonebook\phone_book.json', 'w', encoding='utf-8') as f:
        json.dump(dip, f)
    return pb

def print_contact(pb):
    if len(pb) > 0:
        print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
        print("-" * 85)
        for item in pb:
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
    else:
        print("Справочник пуст!")
    return pb

def delete_contact(pb):
    query = str(input("\nПожалуйста, введите фамилию контакта, который вы хотите удалить: "))
    temp = 0
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            print(pb.pop(i))
            print("\nЭтот запрос был удален")
            return pb
    if temp == 0:
        print("Извините, вы ввели неверный запрос.\
    Пожалуйста, перепроверьте и повторите попытку позже.")
    return pb

def search_contact(pb):
# Эта функция ищет существующий контакт и отображает результат
    choice = int(input("\nВведите критерии поиска\
    \n1. Фамилию\n2. Имя\n3. Номер\n4. Категория(Семья/Друзья/Работа/Другое)\
    \nПожалуйста, введите: "))
    temp = []
    check = -1
    if choice == 1:
        query = str(input("Пожалуйста, введите фамилию контакта, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])
    elif choice == 2:
        query = str(input("Пожалуйста, введите имя контакта, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])
    elif choice == 3:
        query = str(input("Пожалуйста, введите номер телефона, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][2]:
                check = i
                temp.append(pb[i])
    elif choice == 4:
        query = str(input("\nПожалуйста, введите категорию контакта, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check = i
                temp.append(pb[i])
    else:
        print("Неверные критерии поиска")
        return -1
    # возврат -1 означает, что поиск не увенчался успехом
    if check == -1:
        return -1
    # возвращение -1 указывает, что запрос не существует в каталоге
    else:
        print_contact.print_contact(temp)
        return check
    return pb

def exit():
    sys.exit("\nБлагодарим вас за использование нашего телефонного справочника.")
