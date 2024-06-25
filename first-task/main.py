import os

CONTACTS_FILE = 'contacts.txt'


def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r', encoding='utf-8') as file:
            for line in file:
                phone, name = line.strip().split(', ')
                contacts.append((phone, name))
    return contacts


def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w', encoding='utf-8') as file:
        for phone, name in contacts:
            file.write(f'{phone}, {name}\n')


def list_contacts():
    contacts = load_contacts()
    if contacts:
        print("Список контактов:")
        for i, (phone, name) in enumerate(contacts, start=1):
            print(f"{i}. {name} - {phone}")
    else:
        print("Список контактов пуст.")


def add_contact():
    phone = input("Введите номер телефона: ")
    name = input("Введите имя контакта: ")
    contacts = load_contacts()
    contacts.append((phone, name))
    save_contacts(contacts)
    print("Контакт добавлен.")


def modify_contact():
    list_contacts()
    index = int(input("Введите номер контакта для изменения: ")) - 1
    contacts = load_contacts()
    if 0 <= index < len(contacts):
        current_phone, current_name = contacts[index]
        phone = input(f"Введите новый номер телефона (старый: {current_phone}): ")
        name = input(f"Введите новое имя контакта (старое: {current_name}): ")

        if not phone:
            phone = current_phone
        if not name:
            name = current_name

        contacts[index] = (phone, name)
        save_contacts(contacts)
        print("Контакт изменен.")
    else:
        print("Неверный номер контакта.")


def delete_contact():
    list_contacts()
    index = int(input("Введите номер контакта для удаления: ")) - 1
    contacts = load_contacts()
    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
        print("Контакт удален.")
    else:
        print("Неверный номер контакта.")


def main():
    while True:
        print("\nВыберите действие:")
        print("1. Вывести список контактов")
        print("2. Добавить контакт")
        print("3. Изменить контакт")
        print("4. Удалить контакт")
        print("5. Выйти")
        choice = input("Введите номер действия: ")

        if choice == '1':
            list_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            modify_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
