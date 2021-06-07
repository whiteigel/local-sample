documents = [{
    "type": "passport",
    "number": "2207 876234",
    "name": "Василий Гупкин"
}, {
    "type": "invoice",
    "number": "11-2",
    "name": "Геннадий Покемонов"
}, {
    "type": "insurance",
    "number": "10006",
    "name": "Аристарх Павлов"
}]

directories = {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': []}

# a- add function


def add_record(documents, directories):
    doc_number = input('Введите номер документа: ')
    doc_type = input('Введите тип документа: ')
    person_name = input('Введите имя владельца: ')
    shelf_num = input('Введите номер полки: ')

    key = shelf_num
    if key in directories:
        directories.setdefault(key, []).append(doc_number)
        new_item = {
            'type': doc_type,
            'number': doc_number,
            'name': person_name
        }
        documents.append(new_item)
        return 'Документ добавлен.'
    return 'Ошибка! Введите существующий номер полки.'


# p- people function


def get_name(persons):
    person_number = input('Введите номер документа: ')
    for person in persons:
        if person_number == person['number']:
            return person['name']
    return 'Документ с данным номером отсутвует.'


# s- shelf function


def get_shelf(directories):
    number = input('Введите номер документа ')
    for key in directories:
        if number in directories.get(key):
            return key
    return 'Документ с данным номером отсутвует.'


# l- list function


def get_list(persons):
    for person in documents:
        elm = person['type']
        number = person['number']
        name = person['name']
        output = print(f'{elm} "{number}" "{name}"')
    return ''


# as- add shelf function


def add_shelf(directories):
    new_dir = input('Введите номер новой полки: ')
    if new_dir in directories.keys():
        return 'Такой номер полки уже существет. Введите другой номер.'
    else:
        directories[new_dir] = []
        return 'Полка добавлена'


# main function


def main(persons):
    while True:
        print()
        print('Доступные команды: p, s, l, a, as, q')
        command = input('Введите команду: ')
        if command == 'p':
            print()
            print(get_name(persons))
        elif command == 's':
            print()
            print(get_shelf(directories))
        elif command == 'l':
            print()
            print(get_list(persons))
        elif command == 'a':
            print()
            print(add_record(documents, directories))
        elif command == 'as':
            print()
            print(add_shelf(directories))
        elif command == 'q':
            print()
            print('Конец работы')
            break


main(documents)
