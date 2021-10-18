documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "10", "name": "Тест1"},
    {"type": "insurance", "number": "11", "name": "Тест2"}
]
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': ["10", "11"]
      }


def find_name_by_number():
    input_document = input("Введите номер документа:")
    for document in documents:
        if input_document == document["number"]:
            print(document["name"])
            return document["name"]
    if input_document != document["number"]:
        print("Введен не верный номер документа.")


def find_directories_by_number():
    input_document = input("Введите номер документа:")
    for key, value in directories.items():
        for x in value:
            if x == input_document:
                print(key)
                return key
    if input_document != x:
        print("Введен не верный номер документа.")


def find_value_in_documents():
    for document in documents:
        for key, value in document.items():
            print(value, " ", end='')
        print()


def add_document_in_documents_and_directories():
    new_document = {}
    new_document["type"] = input("Введите тип документа:")
    new_document["number"] = input("Введите номер документа:")
    new_document["name"] = input("Введите имя сотрудника:")
    documents.append(new_document)
    while True:
        x = str(input("Введите номер полки:"))
        if x not in directories:
            if input("Создать новую полку?").capitalize() == "Yes":
                number = 1
                while number >= 1:
                    if str(number) not in directories:
                        directories[str(number)] = list(new_document["number"])
                        break
                    else:
                        number += 1
            break
        else:
            directories[x].append(new_document["number"])
            break
    print(directories)


def del_doc_and_dir():
    while True:
        x = input("Введите номер документа:")
        for document in documents:
            if document["number"] == x:
                print(f"Была удалена запись {document} из документов.")
                del documents[documents.index(document)]
                break
        for key, value in directories.items():
            for hz in value:
                if hz == str(x):
                    print(f"Была удалена запись '{hz}' с полки '{key}'.")
                    del value[value.index(hz)]
                    return
        if document["number"] != x or hz != x:
            print("Введен не верный номер документа.")
            continue


def move_doc_in_docks_and_directories():
    while True:
        number_dock = input('Введите номер документа. :')
        target_directories = input('В на какую полку переместить? :')
        for key, value in directories.items():
            for x in value:
                if x == number_dock:
                    print(f"Была перемещена запись '{x}' с полки '{key}' на полку '{target_directories}'.")
                    del value[value.index(x)]
                    directories[target_directories].append(number_dock)
                    print(directories)
                    return key
        if number_dock != x or target_directories != key:
            print("Введены не верные данные.")
            continue
        # elif :
        #     print("Введена не существующая полка.")



def main():
    while True:
        user_input = input("Введите команду:").lower()
        if user_input == "p" or user_input == "people":
            find_name_by_number()
        elif user_input == "s" or user_input == "shelf":
            find_directories_by_number()
        elif user_input == "l" or user_input == "list":
            find_value_in_documents()
        elif user_input == "a" or user_input == "add":
            add_document_in_documents_and_directories()
        elif user_input == "d" or user_input == "delete":
            del_doc_and_dir()
        elif user_input == "m" or user_input == "move":
            move_doc_in_docks_and_directories()
        # elif user_input == "as" or user_input == "add shelf":
        #
        elif user_input == "quit" or user_input == "exit":
            break
        else:
            print("Введена не верная команда.")


main()

