import comands

print("Добрый день!")
ch = 1
pb = comands.initial_phonebook()
while ch in (1, 2, 3, 4, 5):
    print("\nВы можете выполнять следующие операции с этой телефонной книгой: ")
    print("1 - Просмотреть все контакты;")
    print("2 - Добавить контакт;")
    print("3 - Удалить контакт;")
    print("4 - Поиск контакта.")
    print("5 - Выход из телефонной книги")
    ch = int(input("Пожалуйста, введите свой выбор: "))
    if ch == 1:
        pb = comands.print_contact(pb)
    elif ch == 2:
        pb = comands.add_contact(pb)
    elif ch == 3:
        pb = comands.delete_contact(pb)
    elif ch == 4:
        d = comands.search_contact(pb)
        if d == -1:
            print("Контакт не существует. Пожалуйста, попробуйте еще раз")
    elif ch == 5:
        comands.exit()
