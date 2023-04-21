import functions


while True:
    action = int(input('1. Вывод, 2. Добавление, 3. Поиск, 4. Удаление, 5. Изменение\n'))
    if action == 1:
        functions.show_data()
    elif action == 2:
        functions.add_data()
    elif action == 3:
        functions.search_data()
    elif action == 4:
        functions.delete_data()
    elif action == 5:
        functions.change_data()
    else:
        print('Bye!')
        break
