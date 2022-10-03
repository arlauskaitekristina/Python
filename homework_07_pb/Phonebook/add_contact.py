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
    with open(r'C:\Users\New\Desktop\VS_Code\python_seminar\homework_07_pb\Phonebook\phoneb.csv', 'a+', encoding='utf-8') as file:
        file.write(f"\n{dip[0]}\n{dip[1]}\n{dip[2]}\n{dip[3]}\n{dip[0]}, {dip[1]}, {dip[2]}, {dip[3]}")
    return pb
    
