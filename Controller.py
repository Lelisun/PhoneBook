import Model
import View



def main_menu():
    while True:
        print('\nГлавное меню:')
        print('1. Добавить контакт')
        print('2. Удалить контакт')
        print('3. Изменить контакт')
        print('4. Найти контакт')
        print('8. Сохранить файл')
        print('0. Выйти из программы')
        choice = int(input('Выберите пункт: '))
        match (choice):
            case 1:
                add_contact()
                print('\nКонтакт добавлен\n')
            case 2:
                remove_contact()
                print('\nКонтакт удален\n')
            case 3:
                change_contact()
            case 4:
                search_contact()

            case 8:
                save_file()
                print('\nФайл сохранен!\n')
            case 0:
                break


def start():
    open_file()
    View.printPhoneBook()
    main_menu()



def open_file():
    with open(Model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        Model.phonebook = contacts_list

def save_file():
    with open(Model.path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(Model.phonebook)))

def add_contact():
    name = input('Введите имя: ')
    last_name = input('Введите отчество: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {last_name}; {surname};  {phone};\n'
    Model.phonebook.append(contact)
    View.printPhoneBook()

def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    Model.phonebook.pop(choice)
    View.printPhoneBook()

def change_contact():

    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))

    contact = Model.phonebook.pop(choice).split(';')
    print(contact)
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    Model.phonebook.insert(choice, ';'.join(contact))
    View.printPhoneBook()


def search_contact():

    flag = 1
    name = input('Введите имя абонента если требуется поиск по номеру телефона нажмите Enter: ')
    for line in Model.phonebook:
        if name in line:
            flag = 0
            print(line)
    if flag: print('такой абонент отсутствует')
    flag2 = 1
    number = input('Введите номер телефона абонента: ')
    for line in Model.phonebook:
        if number in line:
            flag2 = 0
            print(line)
    if flag2: print('такой абонент отсутствует')