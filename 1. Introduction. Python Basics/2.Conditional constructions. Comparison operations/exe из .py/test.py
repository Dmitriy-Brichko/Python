import time


month = input('Введите месяц рождения, например "Январь". :')
day = int(input('Введите дату рождения, например "31". :'))

if 0 < day < 30:
    if 1<= day <= 29:
        if month == 'Февраль' or month == 'февраль':
            if 20 <= day <= 29:
                print('Рыбы')
            else:
                print('Водолей')
elif 0 < day < 31:
    if 1<= day <= 30:
        if month == 'Апрель' or month == 'апрель':
            if 20 <= day <= 30:
                print('Телец')
            else:
                print('Овен')
        if month == 'Июнь' or month == 'июнь':
            if 21 <= day <= 30:
                print('Рак')
            else:
                print('Близнецы')
        if month == 'Сентябрь' or month == 'сентябрь':
            if 23 <= day <= 30:
                print('Весы')
            else:
                print('Дева')
        if month == 'Ноябрь' or month == 'ноябрь':
            if 23 <= day <= 30:
                print('Стрелец')
            else:
                print('Скорпион')
elif 0 < day < 32:
    if 1<= day <= 31:
        if month == 'Январь' or month == 'январь':
            if 20 <= day <= 31:
                print('Водолей')
            elif 1<= day <= 19:
                print('Козерог')
        if month == 'Март' or month == 'март':
            if 21 <= day <= 31:
                print('Овен')
            else:
                print('Рыбы')
        if month == 'Май' or month == 'май':
            if 21 <= day <= 31:
                print('Близнецы')
            else:
                print('Телец')
        if month == 'Июль' or month == 'июль':
            if 23 <= day <= 31:
                print('Лев')
            else:
                print('Рак')
        if month == 'Август' or month == 'август':
            if 23 <= day <= 31:
                print('Дева')
            else:
                print('Лев')
        if month == 'Октябрь' or month == 'октябрь':
            if 24 <= day <= 31:
                print('Скорпион')
            else:
                print('Весы')
        if month == 'Декабрь' or month == 'декабрь':
            if 21 <= day <= 31:
                print('Козерог')
            else:
                print('Стрелец')
elif 0 > day:
    print('Отрицательный день?')
    time.sleep(2)
    print('Вы из прошлого...?)')
    time.sleep(2)
    print('Запускай заново!')
    time.sleep(4)
    print('Чего ждем?')
    time.sleep(5)
    print('...')
elif str(day) > '31' or str(day)[1] == [2, 3, 4]:
    print('В', (month + 'е'), 'не', day, 'дня!')
    time.sleep(2)
    print('Запускай заново!')
    time.sleep(4)
    print('Чего ждем?')
    time.sleep(5)
    print('...')
    # elif str(day)[1] == [5, 6, 7, 8, 9, 0]
    #     print('В ', (month + 'е'), 'не', day, 'дней!')
    #     time.sleep(2)
    #     print('Запускай заново!')
    #     time.sleep(4)
    #     print('Чего ждем?')
    #     time.sleep(5)
    #     print('...')
    # else:
    #     print('В ', (month + 'е'), 'не', day, 'день!')
    #     time.sleep(2)
    #     print('Запускай заново!')
    #     time.sleep(4)
    #     print('Чего ждем?')
    #     time.sleep(5)
    #     print('...')
time.sleep(00)

# if month == 'Январь' or month == 'январь':
#     if 20 <= day <= 31:
#         print('Водолей')
#     elif day > 31:
#         print('В Январе 31 день!')
#         time.sleep(2)
#         print('Запускай заново!')
#         time.sleep(3)
#         print('Чего ждем?')
#         time.sleep(5)
#         print('...')
#     else:
#         print('Козерог')
# if month == 'Февраль' or month == 'февраль':
#     if 20 <= day <= 29:
#         print('Рыбы')
#     else:
#         print('Водолей')
# if month == 'Март' or month == 'март':
#     if 21 <= day <= 31:
#         print('Овен')
#     else:
#         print('Рыбы')
# if month == 'Апрель' or month == 'апрель':
#     if 20 <= day <= 30:
#         print('Телец')
#     else:
#         print('Овен')
# if month == 'Май' or month == 'май':
#     if 21 <= day <= 31:
#         print('Близнецы')
#     else:
#         print('Телец')
# if month == 'Июнь' or month == 'июнь':
#     if 21 <= day <= 30:
#         print('Рак')
#     else:
#         print('Близнецы')
# if month == 'Июль' or month == 'июль':
#     if 23 <= day <= 31:
#         print('Лев')
#     else:
#         print('Рак')
# if month == 'Август' or month == 'август':
#     if 23 <= day <= 31:
#         print('Дева')
#     else:
#         print('Лев')
# if month == 'Сентябрь' or month == 'сентябрь':
#     if 23 <= day <= 30:
#         print('Весы')
#     else:
#         print('Дева')
# if month == 'Октябрь' or month == 'октябрь':
#     if 24 <= day <= 31:
#         print('Скорпион')
#     else:
#         print('Весы')
# if month == 'Ноябрь' or month == 'ноябрь':
#     if 23 <= day <= 30:
#         print('Стрелец')
#     else:
#         print('Скорпион')
# if month == 'Декабрь' or month == 'декабрь':
#     if 21 <= day <= 31:
#         print('Козерог')
#     else:
#         print('Стрелец')
# time.sleep(60)