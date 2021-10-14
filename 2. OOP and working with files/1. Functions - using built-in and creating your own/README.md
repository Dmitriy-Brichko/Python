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


```
## Домашняя работа
### Задача №1
#### Дан список с в
```python3


```