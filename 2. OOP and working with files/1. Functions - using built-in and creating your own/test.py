
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "10", "name": "Тест1"},
    {"type": "insurance", "number": "10", "name": "Тест2"}
]
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def find_name_by_number():
    input_document = input("Введите номер документа:")
    for document in documents:
        doc = document["number"]
        name = document["name"]
        if input_document == doc:
            print(name)
    if input_document != doc:
        print("Введен не верный номер документа.")


def main():
    while True:
        user_input = input("Введите команду:")
        if user_input == "p" or user_input == "people":
            find_name_by_number()
        # elif user_input == "s" or user_input == "shelf":
        #     print("zqwe")

        # elif user_input == "p" or user_input == "people":
        #     print("zqwe")
        #
        # elif user_input == "p" or user_input == "people":
        #     print("zqwe")
        #
        #
        # elif user_input == "p" or user_input == "people":
        #     print("zqwe")
        #
        # elif user_input == "p" or user_input == "people":
        #     print("2")
        #
        # elif user_input == "p" or user_input == "people":
        #     print("1")
        # else:
        #     print("Введены не верные данные.")


main()
