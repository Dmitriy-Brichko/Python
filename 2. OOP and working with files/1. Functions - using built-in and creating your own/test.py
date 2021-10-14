# names = ("Иван", "Мария", "Петр", "Илья")
# def thesaurus(names):


number = 5  # Глобальная переменная
power = 3  # Глобальная переменная


def power_2():
    number = 6  # Локальная переменная
    power = 2  # Локальная переменная
    return number ** power


print(number ** power)  # Ищет глобальные переменные

print(power_2())  # Ищет локальные переменные, если их нет, то ищет глобальные
