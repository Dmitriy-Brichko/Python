## Работа на лекции
```python3
# В результате операций:
a = 1
b = 2
print(a > b)
print(a < b)
print(a == b) # сравнение чисел (равно)
print(a >= b) # >=
print(a <= b) # <=
print(a != b) # != не равно
```
```python3
# получаем булевое (логическое, их всего два) значение True / False
print(2 > 1)
print(10 == 10)
print(10 != 10)
print(5 > 4 < 15)
test1 = 10 < 9
print(test1)
```
```python3
# Чем дальше стоит буква от начала алфавита тем она больше
length = len('test ')

print('c' > 'a')
print('b' > 'B')
print('abc' > 'aba') # идет сравнение до первого различного символа
print(len('abc') > len('aba')) # len определяет длину строки(все символы и пробелы тоже)
print(length)
```
```python3
# Логические операторы
print(True and True)
print(True and False)
print(True or False)
print(not True) # not меняет значение, если было True то станет False
print((9 > 7) and (2 < 4))
print((8 == 8) or (6 != 6))
print(not(3 <= 1))
print(bool(3)) # только 0 будет False
print(bool('тест'))
```
```python3
# Условные конструкции
x = 7
if x % 2 == 0:
    print(x, ' - четное число')
else:  # else (во всех остальных случаях)
    print(x, '- нечетное число')
    
###
x = int(input('Введите координату X:'))
y = int(input('Введите координату Y:'))
if (x > 0) and (y > 0):
    print('Первая часть')
elif (x < 0) and (y < 0):
    print('Третья часть')
elif y < 0:  # elif (elseif)
    print('Вторая часть')
else:
    print('Четвертая часть')
    
###
age = 17
height = 182

if 18 <= age < 27:
    if height < 170:
        print('В танкисты')
    elif height < 185:
        print('На флот')
    elif height < 200:
        print('Десантники')
    else:
        print('В другие войска')
else:
    print('Не призывной возраст')

###
# число (не 0) или символ это True
name = input('Введите свое имя:')

if name:  # имя True то,
    print('Привет', name)
else:  # имя False, то,
    print('Привет, Мир!')

###
number = int(input('Ведите число'))

if number:
    print('Число', number)
else:
    print('Число равно нулю')

```
```python3
a_1 = input('ВВедите первое число:')
b_2 = input('ВВедите второе число:')
c_3 = input('ВВедите третье число:')

if (a_1 > b_2) and (a_1 > c_3):
    print(a_1, '- самое большое число')
elif b_2 > c_3:
    print(b_2, '- самое большое число')
else:
    print(c_3, '- самое большое число')

```
```Python3
# Счастливый билет или нет?
number = input('Введите номер билета:')
number = str(number)
one = int(number[0])
two = int(number[1])
three = int(number[2])
four = int(number[3])
five = int(number[4])
six = int(number[5])

if (one + two + three) == (four + five + six):
    print('Счастливый билет!')
else:
    print('В следующий раз повезет!')

# еще вариант
number = int(input('Введите номер билета:'))

number_1 = number // 100000  # цело численное деление
number_2 = number // 10000 % 10
number_3 = number // 1000 % 10
number_4 = number // 100 % 10
number_5 = number // 10 % 10
number_6 = number % 10
number_123 = number_1 + number_2 + number_3
number_456 = number_4 + number_5 + number_6
if number_123 == number_456:
    print('Счастливый билет')
else:
    print('Не счастливый билет')

```
## Задача 1
```python3
n = int(input('Введите число :'))
if n % 2 == 0:
    if 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')
else:
    print('Weird')

```
## Задача 2. Годен на службу или нет.
```python3
age = int(input('Введите Ваш возраст:'))
height = int(input('Введите Ваш рост:'))
how_many_children = int(input('Сколько у Вас детей? '))
study_or_no = input('Вы обучаетесь сейчас? Ответе "Да" или "Нет". :')

if 18 <= age < 27:
    if study_or_no == 'Нет':
        if how_many_children <= 2:
            if height < 170:
                print('В танкисты')
            elif height < 185:
                print('На флот')
            elif height < 200:
                print('Десантники')
            else:
                print('В другие войска')
        else:
            print('Не годен. 2 или более детей')
    else:
        print('Не годен. Проходит обучение')
else:
    print('Не годен. Не призывной возраст')

```
## Задание №3. Определение знака зодиака.
```python3
month = input('Введите месяц рождения, например "Январь". :')
day = int(input('Введите дату рождения, например "31". :'))
if month == 'Январь' or month == 'январь':
    if 20 <= day:
        print('Водолей')
    else:
        print('Козерог')
if month == 'Февраль' or month == 'февраль':
    if 20 <= day:
        print('Рыбы')
    else:
        print('Водолей')
if month == 'Март' or month == 'март':
    if 21 <= day:
        print('Овен')
    else:
        print('Рыбы')
if month == 'Апрель' or month == 'апрель':
    if 20 <= day:
        print('Телец')
    else:
        print('Овен')
if month == 'Май' or month == 'май':
    if 21 <= day:
        print('Близнецы')
    else:
        print('Телец')
if month == 'Июнь' or month == 'июнь':
    if 21 <= day:
        print('Рак')
    else:
        print('Близнецы')
if month == 'Июль' or month == 'июль':
    if 23 <= day:
        print('Лев')
    else:
        print('Рак')
if month == 'Август' or month == 'август':
    if 23 <= day:
        print('Дева')
    else:
        print('Лев')
if month == 'Сентябрь' or month == 'сентябрь':
    if 23 <= day:
        print('Весы')
    else:
        print('Дева')
if month == 'Октябрь' or month == 'октябрь':
    if 24 <= day:
        print('Скорпион')
    else:
        print('Весы')
if month == 'Ноябрь' or month == 'ноябрь':
    if 23 <= day:
        print('Стрелец')
    else:
        print('Скорпион')
if month == 'Декабрь' or month == 'декабрь':
    if 21 <= day:
        print('Козерог')
    else:
        print('Стрелец')

```