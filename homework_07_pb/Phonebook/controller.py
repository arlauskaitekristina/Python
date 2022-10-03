import initial_phonebook
import print_contact
import add_contact
import delete_contact
import search_contact
import exit

print("Добрый день!")
ch = 1
pb = initial_phonebook.initial_phonebook()
while ch in (1, 2, 3, 4, 5):
    print("\nВы можете выполнять следующие операции с этой телефонной книгой: ")
    print("1 - Просмотреть все контакты;")
    print("2 - Добавить контакт;")
    print("3 - Удалить контакт;")
    print("4 - Поиск контакта.")
    print("5 - Выход из телефонной книги")
    ch = int(input("Пожалуйста, введите свой выбор: "))
    if ch == 1:
        pb = print_contact.print_contact(pb)
    elif ch == 2:
        pb = add_contact.add_contact(pb)
    elif ch == 3:
        pb = delete_contact.delete_contact(pb)
    elif ch == 4:
        d = search_contact.search_contact(pb)
        if d == -1:
            print("Контакт не существует. Пожалуйста, попробуйте еще раз")
    elif ch == 5:
        exit.exit()
