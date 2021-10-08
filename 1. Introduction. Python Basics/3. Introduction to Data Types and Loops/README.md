## Работа на лекции
##### Типы данных
```python3
int()  # (integer) - целые числа
float()  # Действительные числа
str()  # (strong) - строки
bool()  # (boolean) - логический тип

# Пример
number = 10
q = 9.8
name = 'Коля'
san = True
print(1 + True)  # True это 1, False это 0

print(number, q, name, san)

```
#### Операции со строками
```python3
my_sting = 'qwe r'

my_sting.upper()  # Приводит строку к верхнему регистру
my_sting.lower()  # Приводит строку к нижнему регистру
my_sting.capitalize()  # Приводит первую букву к верхнему регистру
my_sting.replace('Что заменить', 'на что заменить')  # Заменяет элемент в строке на указанный
len(my_sting)  # Позволяет определить длину строки (количество символов в ней)

# Пример
my_sting = 'hello World'
# () - это параметры, не для всех методов есть обязательные параметры, поэтому пустые скобки
print(my_sting.upper()) 
print(my_sting.lower())
print(my_sting.capitalize())
print(my_sting.title())  # Оба слова с большой буквы
print(my_sting.replace('hello', 'goodbye'))
print(len(my_sting))

# Форматирование строк (F-строки)
name= 'коля'
age = 13
lang = 'python'

my_sting = f'Hello, my name is {name.title()}, I know {lang} a bit, I am {age} year old'
print(my_sting)

```
#### Индексация и среды строк
```python3
my_string = 'индекс'
# 0  1  2  3  4  5
# и  н  д  е  к  с
#-6 -5 -4 -3 -2 -1
print(my_string[0] == my_string[-6])

# Срез строк
print(my_string[1:3])  # 1 - первый элемент в списке, 3-элемент перед которым закончится срез
print(my_string[0:6:2])  # 2 - шаг среза
print(my_string[3:])  # 3 - с 3 элемента до конца
print(my_string[:3])  # 3 - с начала до 3 элемента
print(my_string[::-1])  # Инвертировать строку

# Список
name_list = [1,'el',3]  # Создали список
del(name_list[2])  # Удаляет элемент из списка по индексу
name_list.remove('el')  # Удаляет указанный элемент из списка
name_list.append('el')  # Добавляет элемент в список
name_list.count('el')  # Считает количество вхождений элемента в список
name_list.index('el')  # Позволяет узнать индекс элемента в списке
name_list.reverse()  # Разворачивает список
sorted(name_list)  #Сортирует список

# Примеры:
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
income_list = [13000, 14000, 14300, 15000, 13800, 13000, 14900, 15200, 15300]
income_by_month = [['Jan', 13000], ['Feb', 14000], ['Mar', 14300], ['Apr', 15000],
                   ['May', 13800], ['Jun', 13000], ['Jul', 14900], ['Aug', 15200], ['Sep', 1500]]
print(month_list[0])
print(income_list[-2])
print(income_by_month[-4])
print(income_by_month[-4][0])
print(income_by_month[-4][0][0])
print(income_by_month[0:2])
income_by_month[0][1] = 13100
print(income_by_month)
income_by_month_2 = [['Now', 15400], ['Dec', 17000]]
income_by_month = income_by_month + income_by_month_2
income_by_month.remove(['Dec', 17000])
del(income_by_month[-1])
print(income_by_month)
income_by_month.append(['Dec', 17000])
income_by_month.insert(1, [12321312])  # Добавляет на позицию 1 12321312
print(income_list.index(13000))  # Найдет только первый
month_list.reverse()  # Эти работают
print(month_list[::-1])  # одинаково
print(sorted(income_list))  # Сортирует по возрастанию
print(sorted(income_list, reverse=True))  # Сортирует по убыванию
income_list.sort()  # Изменит income_list
queries_string = "смотреть сериалы онлайн, новости спорта, афиша, кино, диалог, доллар, по питону"
print(queries_string.split(','))  # Разделяет строку на список
print('\t'.join(['Строка 1', 'Строка 2', 'строка 3']))  # Разделяет список на строку (экранированная последовательность)

```
#### Кортежи (tuples)
```python3
salary_tuple = (1000, 1200, 1300, 900, 800)
print(salary_tuple[0])
# salary_tuple[0] = 500  # Кортежи нельзя менять!
print(type(salary_tuple))
my_list = list(salary_tuple)
print(type(my_list))
my_list = tuple(my_list)
print(type(my_list))
# Функция Zip
names = ['Robert', 'Jane', 'Liza', 'Richard', 'Anya']
salary_by_names = zip(salary_tuple, names)
test = list(salary_by_names)
print(test)

company_tuple = ('Orange', 1000000, 20000)
company_name, yandex, google = company_tuple
print(company_name)
print(yandex)
print(google)

print('Orange' in company_tuple)  # Покажет, есть ли 'Orange' в company_tuple
print('range' not in company_tuple)  # Покажет, нет ли 'range' в company_tuple

```
#### Циклы
```python3
# while
# Покажет:4 3 2 1 0
x = 5
while x != 0:
    x -= 1
    print(x)
# от 7 до 1 расскажет четные числа или нечетные
x = 7
while x != 0:
    if x % 2 == 0:
        print(x, '- четное число')
    else:
        print(x, '- нечетное число')
    x -= 1
# сумма введенных чисел до введенного 0
number = 0
number_1 = int(input('Введите число:'))
number_2 = ''
while number_2 != 0:
    number_2 = int(input('Введите следующее число:'))
    number += number_2
number += number_1
print(f'Сумма введенных Вами чисел равна:{number}')
###
while True:
    x = input('Введите команду:')
    if x == '1':
        pass
    elif x == '2':
        pass
    elif x == 'quit':
        break
```
```python3
# for
company_name = 'Orange'
for letter in company_name:
    letter = letter.capitalize()
    print(letter)  # Выведет каждую букву company_name с большой буквы с новой строки
company_name = 'Orange'
for qwerty in company_name:
    qwerty = qwerty.capitalize()
    print(qwerty, end='')
    
# С помощью for достаем из списка информацию
companies_capitalization = [
    ['Orange', 1.3],
    ['Maxisoft', 1.5],
    ['Headbook', 0.8],
    ['Nicola', 2.2]
]
# 1
for company in companies_capitalization:
    print(company)  # (Информационная строка!)В company поместились все списки companies_capitalization
    print(f"{company[0]}'s capitalization is {company[1]}")
# 2
for company, cap in companies_capitalization:  # Если два элемента в списке
    print(f"{company}'s capitalization is {cap} ")

# Цикл прервется, как только встретит пробел
phrase = '640kb must have'
for letter in phrase:
    if letter == ' ':
        break
    print(letter, end='')
# Цикл продолжится без пробела
phrase = '640kb must have'
for letter in phrase:
    if letter == ' ':
        continue
    print(letter, end='')
# pass говорит циклу - ничего с этим не делай
phrase = '640kb must have'
for letter in phrase:
    if letter == ' ':
        pass
    print(letter, end='')
    
# Цикл вложенный в цикл
professions = ['IT', 'Физика', 'Математика']
persons = [
    ['Гейтс', 'Джобс', 'Возняк'],
    ['Эйнштейн', 'Фейнман'],
    ['Эвклид', 'Ньютон']
    ]
for pro, names in zip(professions, persons):
    print(f'{pro}:')
    for name in names:
        print(name)
    print()

```