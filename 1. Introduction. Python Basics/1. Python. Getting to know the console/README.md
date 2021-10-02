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
#считает площать квадрата
lehgth = input('Введите длину стороны квадрата :')
def isfloat(lehgth):
    try:
        float(lehgth)
        return False
    except 'Введите длину стороны квадрата':  # !!!!не понял как работает строка
        return True
print(float(lehgth) * 2.0)

#считает площадь прямоугольника
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
```python3

```