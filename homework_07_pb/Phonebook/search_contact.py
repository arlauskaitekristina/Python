import print_contact
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