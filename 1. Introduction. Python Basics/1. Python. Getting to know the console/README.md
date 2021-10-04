### Работа на лекции
```bash
#print('Hi, PY-35')
#print('Hello python')
#print(2 + 2)
#print(2 - 1)
#print(2 * 3)
#print(2 ** 6) #возведение в степень **
#print(11 / 4)
#print(11 // 4) #получить целое число
#print(11 % 4) #получаем остаток от деления
#print(2 + 2 * 2)
#print((2 + 2) * 2)
#print(10 / 2 // 4)
#my_name = 'Дмитрий'
#print(my_name)
#salary = '1000000 $'
#print(salary)
#my_teams = 'Google'
#print(my_teams)
#print('Hi,', 'my name is', my_name,',', 'I take salary', salary, 'in', my_teams)
#print('Hi,', 'my name is', my_name, ',', 'I take salary', salary, 'in', my_teams, sep='!') # sep='Меняет разделитель'
#print('Hi,', 'my name is', my_name)
#
#age = input('Сколько тебе лет?')
#age = int(age)
#print(type(age))
#print(age)
#print(age - 18)
#age = input('Введите ваш возрост')
#name = 'Dima'
#print(name.find('i')) #Поиск по i в переменной
#print(name + ' 12')
#print('Hello' * 2) #Мультиплицирование

```

### Задача 1
```python3
# Say "Hello, World!" With Python

my_string = "Hello, World!"
print(my_string)


# Arithmetic Operators

a = 3
b = 5
print(a + b)
print(a - b)
print(a * b)

```
### Задача 2

```python3
# считает площать квадрата
try:
    lehgth = float(input('Введите длину стороны квадрата :'))
    print(float(lehgth) * 2.0)
except ValueError:
    print('Введено не число')
    print('Длина вводится целым или десятичным цислом!')
    lehgth = float(input('Введите длину стороны квадрата :'))
    print(float(lehgth) * 2.0)

#считает площадь прямоугольника
try:
    lehgth_a = float(input('Введите длину прямоугольника :'))
    lehgth_b = float(input('Введите ширину прямоугольника :'))
    print(float(lehgth_a) * float(lehgth_b))
except ValueError:
    print('Введено не число!!!')
    print('Длина вводится целым или десятичным цислом!')
    lehgth_a = float(input('Введите длину прямоугольника :'))
    lehgth_b = float(input('Введите ширину прямоугольника :'))
    print(float(lehgth_a) * float(lehgth_b))
    
    
# или так

lehgth_a = input('Введите длину стороны Прямоугольника :')
lehgth_b = input('Введите длину стороны Прямоугольника :')
def isfloat_a(lehgth_a):
    try:
        float(lehgth_a)
        return False
    except 'Введите длину стороны квадрата':  # !!!!не понял как работает строка
        return True
def isfloat_b(lehgth_b):
    try:
        float(lehgth_b)
        return False
    except 'Введите ширину стороны квадрата':  # !!!!не понял как работает строка
        return True
print(float(lehgth_a) * float(lehgth_b))

```
### Задача 3
```python3
# Считает накопления за год
import time


try:
    wages = float(input('Укажите Вашу заработную плату в месяц в рублях. :'))
except ValueError:
    print('Введено не число!!!')
    print('Значение вводится целым или десятичным цислом!')
    wages = float(input('Укажите Вашу заработную плату в месяц в рублях. :'))

try:
    percent_from_wages_for_mortgage = float(input('Какой процент(%) от зп у Вас уходит на себя? :'))
except ValueError:
    print('Введено не число!!!')
    print('Значение вводится целым или десятичным цислом!')
    percent_from_wages_for_mortgage = input('Какой процент(%) от зп у Вас уходит на себя? :')

try:
    percent_from_wages_for_live = float(input('Какой процент(%) от зп у Вас уходит "на жизнь"? :'))
except ValueError:
    print('Введено не число!!!')
    print('Значение вводится целым или десятичным цислом!')
    percent_from_wages_for_live = input('Какой процент(%) от зп у Вас уходит "на жизнь"? :')

money_for_mortgage = float(wages) * float(percent_from_wages_for_mortgage) / 100.0
money_for_mortgage_in_year = float(money_for_mortgage * 12.0)
money_for_live = float(wages) * float(percent_from_wages_for_live) / 100.0
savings_money_for_month = float(wages) - float(money_for_mortgage) - float(money_for_live)
savings_money_for_year = float(savings_money_for_month) * 12.0
print('Потрачено денег в год на себя' ,money_for_mortgage_in_year, 'р.')
print('Накоплено денег за год', savings_money_for_year, 'р.')
time.sleep(900000)

```