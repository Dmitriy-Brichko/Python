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