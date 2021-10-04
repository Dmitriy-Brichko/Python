import time


month = input('Введите месяц рождения, например "Январь". :')
day = int(input('Введите дату рождения, например "31". :'))

if month == 'Январь' or month == 'январь':
    if 20 <= day <= 31:
        print('Водолей')
    elif 1 <= day <= 19:
        print('Козерог')
elif month == 'Февраль' or month == 'февраль':
    if 20 <= day <= 29:
        print('Рыбы')
    elif 1 <= day <= 19:
        print('Водолей')
    elif day > 29:
        if str(day)[1] == '2' or str(day)[1] == '3' or str(day)[1] == '4':
            print('В', (month + 'е'), 'не', day, 'дня!')
            time.sleep(2)
            print('Запускай заново!')
            time.sleep(4)
            print('Чего ждем?')
            time.sleep(5)
            print('...')
        elif str(day)[1] == '5' or str(day)[1] == '6' or str(day)[1] == '7' \
                or str(day)[1] == '8' or str(day)[1] == '9' or str(day)[1] == '0':
            print('В', (month + 'е'), 'не', day, 'дней!')
            time.sleep(2)
            print('Запускай заново!')
            time.sleep(4)
            print('Чего ждем?')
            time.sleep(5)
            print('...')
elif month == 'Март' or month == 'март':
    if 21 <= day <= 31:
        print('Овен')
    elif 1 <= day <= 20:
        print('Рыбы')
elif month == 'Апрель' or month == 'апрель':
    if 20 <= day <= 30:
        print('Телец')
    elif 1 <= day <= 19:
        print('Овен')
    elif day > 30:
        if str(day)[1] == '2' or str(day)[1] == '3' or str(day)[1] == '4':
            print('В', (month + 'е'), 'не', day, 'дня!')
            time.sleep(2)
            print('Запускай заново!')
            time.sleep(4)
            print('Чего ждем?')
            time.sleep(5)
            print('...')
        elif str(day)[1] == '5' or str(day)[1] == '6' or str(day)[1] == '7' \
                or str(day)[1] == '8' or str(day)[1] == '9' or str(day)[1] == '0':
            print('В', (month + 'е'), 'не', day, 'дней!')
            time.sleep(2)
            print('Запускай заново!')
            time.sleep(4)
            print('Чего ждем?')
            time.sleep(5)
            print('...')
elif month == 'Май' or month == 'май':
    if 21 <= day <= 31:
        print('Близнецы')
    elif 1 <= day <= 20:
        print('Телец')
elif month == 'Июнь' or month == 'июнь':
    if 21 <= day <= 30:
        print('Рак')
    elif 1 <= day <= 20:
        print('Близнецы')
    elif day > 30:
        if str(day)[1] == '2' or str(day)[1] == '3' or str(day)[1] == '4':
            print('В', (month + 'е'), 'не', day, 'дня!')
            time.sleep(2)
            print('Запускай заново!')
            time.sleep(4)
            print('Чего ждем?')
            time.sleep(5)
            print('...')
        elif str(day)[1] == '5' or str(day)[1] == '6' or str(day)[1] == '7' \
                or str(day)[1] == '8' or str(day)[1] == '9' or str(day)[1] == '0':
            print('В', (month + 'е'), 'не', day, 'дней!')
            time.sleep(2)
            print('Запускай заново!')
            time.sleep(4)
            print('Чего ждем?')
            time.sleep(5)
            print('...')
elif month == 'Июль' or month == 'июль':
    if 23 <= day <= 31:
        print('Лев')
    elif 1 <= day <= 22:
        print('Рак')
elif month == 'Август' or month == 'август':
    if 23 <= day <= 31:
        print('Дева')
    elif 1 <= day <= 22:
        print('Лев')
elif month == 'Сентябрь' or month == 'сентябрь':
    if 23 <= day <= 30:
        print('Весы')
    elif 1 <= day <= 22:
        print('Дева')
    elif day > 30:
        if str(day)[1] == '2' or str(day)[1] == '3' or str(day)[1] == '4':
            print('В', (month + 'е'), 'не', day, 'дня!')
            time.sleep(2)
            print('Запускай заново!')
            time.sleep(4)
            print('Чего ждем?')
            time.sleep(5)
            print('...')
        elif str(day)[1] == '5' or str(day)[1] == '6' or str(day)[1] == '7' \
                or str(day)[1] == '8' or str(day)[1] == '9' or str(day)[1] == '0':
            print('В', (month + 'е'), 'не', day, 'дней!')
            time.sleep(2)
            print('Запускай заново!')
            time.sleep(4)
            print('Чего ждем?')
            time.sleep(5)
            print('...')
elif month == 'Октябрь' or month == 'октябрь':
    if 24 <= day <= 31:
        print('Скорпион')
    elif 1 <= day <= 23:
        print('Весы')
elif month == 'Ноябрь' or month == 'ноябрь':
    if 23 <= day <= 30:
        print('Стрелец')
    elif 1 <= day <= 22:
        print('Скорпион')
    elif day > 30:
        if str(day)[1] == '2' or str(day)[1] == '3' or str(day)[1] == '4':
            print('В', (month + 'е'), 'не', day, 'дня!')
            time.sleep(2)
            print('Запускай заново!')
            time.sleep(4)
            print('Чего ждем?')
            time.sleep(5)
            print('...')
        elif str(day)[1] == '5' or str(day)[1] == '6' or str(day)[1] == '7' \
                or str(day)[1] == '8' or str(day)[1] == '9' or str(day)[1] == '0':
            print('В', (month + 'е'), 'не', day, 'дней!')
            time.sleep(2)
            print('Запускай заново!')
            time.sleep(4)
            print('Чего ждем?')
            time.sleep(5)
            print('...')
elif month == 'Декабрь' or month == 'декабрь':
    if 21 <= day <= 31:
        print('Козерог')
    elif 1 <= day <= 20:
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
elif day > 31:
    if str(day)[1] == '2' or str(day)[1] == '3' or str(day)[1] == '4':
        print('В', (month + 'е'), 'не', day, 'дня!')
        time.sleep(2)
        print('Запускай заново!')
        time.sleep(4)
        print('Чего ждем?')
        time.sleep(5)
        print('...')
    elif str(day)[1] == '5' or str(day)[1] == '6' or str(day)[1] == '7'\
            or str(day)[1] == '8' or str(day)[1] == '9' or str(day)[1] == '0':
        print('В', (month + 'е'), 'не', day, 'дней!')
        time.sleep(2)
        print('Запускай заново!')
        time.sleep(4)
        print('Чего ждем?')
        time.sleep(5)
        print('...')
    else:
        print('В', (month + 'е'), 'не', day, 'день!')
        time.sleep(2)
        print('Запускай заново!')
        time.sleep(4)
        print('Чего ждем?')
        time.sleep(5)
        print('...')
else:
    print('Плохо, когда не знаешь название месяцов...')
    time.sleep(2)
    print('Перезапускай и давай по новой')
    time.sleep(3)
    print('У тебя получится!')
    time.sleep(5)
    print('ну же...')
time.sleep(30)
