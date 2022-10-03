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