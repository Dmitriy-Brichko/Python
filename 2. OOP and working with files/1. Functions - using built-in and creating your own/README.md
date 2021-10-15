## Работа на лекции
##### Что такое функция
```python3
# def - определить
# give_name_function - имя функции (действие)
def give_name_function(number):
    result = number ** 2  # ** в этой строке ^
    return result  # Возвращает значение из функции, останавливает работу функции

```
```python3
def square(number):
    result = number ** 2
    return result


print(square(7))
res = square(7)
print(res)

help(print)

```
#### Docstring - строка документации
```python3
def square(number):
    """
    this is my first function
    """
    result = number ** 2
    return result


help(square)

```
#### Параметры функции '()' - может быть более 1 параметра или нисколько
```python3
def square_2():
    user_input = int(input('Введите число'))
    result = user_input ** 2
    return result


print(square_2())

def power(num_1, num_2=2):  # num_2=2 - сделали num_2 параметром по умолчанию
    return num_1 ** num_2


print(power(4, 5))  # Но сдесь параметр по умолчанию num_2 мы перезаписали на 5

```
#### Тип данных None - None означает отсутствие значения. Если в функции нет return, либо он пустой, то она возвращает None.
```python3
def square_2(number):
    result = number ** 2
    print(result)  # Здесь получим "25"

    
print(square_2(3))  # Здесь получим "None"

```
#### Области видимости - scope. Глобальная, локальная, 
```python3
# names = ("Иван", "Мария", "Петр", "Илья")
# def thesaurus(names):


number = 5  # Глобальная переменная
power = 3  # Глобальная переменная


def power_2():
    number = 6  # Локальная переменная
    power = 2  # Локальная переменная
    some_nomber = 1  # Локальная переменная
    return number ** power


print(number ** power)  # Ищет глобальные переменные
print(power_2())  # Ищет локальные переменные, если их нет, то ищет глобальные
# print(some_nomber)  # Будет ошибка! Из-за того, что мы обращяемся из глобального контекста, а переменная в локальном.

```
#### Операторы global и nonlocal
```python3
name = "James"
def say_hi():
    global name  # Перезапишем глобальную переменную name
    name = 'Oleg'
    print(f"Hello, {name}")

print(name)  # До вызова функции say_hi переменная name не перезаписана
say_hi()
print(name)

def say_hi():
    name = 'Oleg'
    def get_name():
        nonlocal name  # Переменная станет не локальной для функции get_name, при этом она станет локальной для say_hi.
        name = input('Ведите имя:')
        return name
    get_name()
    print(f"Hello, {name}")

say_hi()

```
#### Если тело функции помещается в одну строку, то можно создать lambda - функцию
```python3
func = lambda x, y: x + y  # lambda
print(func(5, 4))

```
## Домашняя работа
#### Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:
```python3
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

```
#### Перечень полок, на которых находятся документы хранится в следующем виде:
```python3
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

```
#### Интересный кейс
```python3
# Считаем среднюю оценку группы по экзамену
students_list = [
    {"name": "Василий", "surname": "Теркин", "gender": "м",
     "program_exp": True, "grade": [8, 8, 9, 10, 9], "exam": 8},
    {"name": "Мария", "surname": "Павлова", "gender": "ж",
     "program_exp": True, "grade": [7, 8, 9, 7, 9], "exam": 9},
    {"name": "Ирина", "surname": "Андреева", "gender": "ж",
     "program_exp": False, "grade": [10, 9, 8, 10, 10], "exam": 7},
    {"name": "Татьяна", "surname": "Сидорова", "gender": "ж",
     "program_exp": False, "grade": [7, 8, 8, 9, 8], "exam": 10},
    {"name": "Иван", "surname": "Васильев", "gender": "м",
     "program_exp": True, "grade": [9, 8, 9, 6, 9], "exam": 5},
    {"name": "Роман", "surname": "Золотарев", "gender": "м",
     "program_exp": False, "grade": [8, 9, 9, 6, 9], "exam": 6},
]

# Нашли среднюю оценку за экзамен
def get_avg_ex_grade(students):
    sum_ex = 0
    for student in students:
        sum_ex += student["exam"]  # Нашли по ключу оценку каждого ученика
    return round(sum_ex / len(students), 2)  # Округлили до двух знаков после запятой


print(get_avg_ex_grade(students_list))

# Нашли среднюю оценку за все домашние работы
def get_avg_hw_grade(students):
    sum_hw = 0
    for student in students:
        sum_hw += sum(student["grade"]) / len(student["grade"])  # Сложили список student["grade"] - [8, 9, 9, 6, 9]
    return round(sum_hw / len(students), 2)


print(get_avg_hw_grade(students_list))

# Нашли среднюю оценку за все домашние работы у девочек или мальчиков или у всех, учитывая опыт.
def get_avg_hw_grade_girl(students, sex=None, exp=None):
    sum_hw = 0
    count = 0
    for student in students:
        if (student["gender"] == sex and exp is None) or\
                (sex is None and exp is None) or\
                (sex is None and student["program_exp"] == exp) or\
                (student["gender"] == sex and student["program_exp"] == exp):
            sum_hw += sum(student["grade"]) / len(student["grade"])
            count += 1
        # elif
    return round(sum_hw / count, 2)


print(get_avg_hw_grade_girl(students_list, "м", False))
print(get_avg_hw_grade_girl(students_list, "ж", True))
print(get_avg_hw_grade_girl(students_list, None, False))
print(get_avg_hw_grade_girl(students_list, exp=True))
print(get_avg_hw_grade_girl(students_list, "м"))
print(get_avg_hw_grade_girl(students_list, "ж"))
print(get_avg_hw_grade_girl(students_list))

```
### Задача №1
#### Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

* p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
* s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
* l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
* a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.

Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.
```python3


```
### Задача №2
* d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
* m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
* as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;
```python3


```