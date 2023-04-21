def show_data() -> None:
    ''' Вывод информации из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def add_data() -> None:
    '''Добавляет информацию в справочник'''
    with open('book.txt', 'a', encoding='utf-8') as f:
        name = input('Введите ФИО: ')
        phone = input('Введите телефон: ')
        f.write(f'\n{name} | {phone}')


def search_data() -> None:
    '''Осуществляет поиск по справочнику'''
    to_find = input('Что хотите найти?: ')
    book_list = []
    with open('book.txt', 'r', encoding='utf-8') as f:
        for line in f:
           book_list.append(line.split(' | '))
    result = search(book_list, to_find)
    for item in result:
        print(*item[1])


def search(book: list, data: str) -> list:
    '''Ищет данные и дает результат с номером строки'''
    res = []
    finded = False
    for item in book:
        if item[0].find(data) != -1:
            res.append((book.index(item),item))
            finded = True
        elif data in item[1]:
            res.append((book.index(item),item))
            finded = True
    if not finded:
        print('Не найдено')
    return res


def change_data() -> None:
    '''По ФИО или телефону меняет данные'''
    to_change = input('ФИО для изменения телефона: ')
    change = input('Новый номер телефона: ')
    book_list = []
    with open('book.txt', 'r', encoding='utf-8') as f:
        for line in f:
           book_list.append(line.split(' | '))
    result = search(book_list, to_change)
    for item in result:
        book_list[item[0]][1] = f'{change}\n'
    with open('book.txt', 'w', encoding='utf-8') as f:
        for line in book_list:
            f.write(" | ".join(line))
        

def delete_data() -> None:
    '''По ФИО или телефону удаляет данные'''
    to_del = input('Что хотите удалить?: ')
    book_list = []
    with open('book.txt', 'r', encoding='utf-8') as f:
        for line in f:
           book_list.append(line.split(' | '))
    result = search(book_list, to_del)
    if len(result) < 1:
        return
    for item in result:
        book_list.pop(item[0])
    with open('book.txt', 'w', encoding='utf-8') as f:
        for line in book_list:
            f.write(" | ".join(line))
    