### Работа на лекции
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
    print('Не счаслиный билет')

```