## Работа на лекции
##### Объекты и классы. Взаимодействие между ними
ООП - объектно ориентированное программирование.

Преподаватель пользуется Jupyter Notebook - ПО в web-интерфейсе.
```python3
print(type("Hello World"))
# <class 'str'> - класс, со своим функционалом.
# Вывести все методы для str
print(dir(str))
```
Классы, экземпляры и атрибуты
```python3
class Character:  # Создали класс
    pass


peter = Character()  # Создали экземпляр
print(type(peter))


class Character:  # Пересоздали класс
    # Создали атрибуты:
    gender = ''
    name = ''
    height = 0
    weight = 0
    hands = 2


peter = Character()  # Пересоздали экземпляр
print(peter.gender)
print(peter.name)
print(peter.height)
print(peter.weight)
print(peter.hands)

# Присваиваем свои атрибуты
peter.name = 'Peter Parker'
peter.gender = 'm'
peter.weight = 70
peter.height = 175

# Добавим персональный атрибут
peter.alias = 'Spider-Man'

print(peter.alias)
print(peter.gender)
print(peter.name)
print(peter.height)
print(peter.weight)
print(peter.hands)

bruce = Character()
bruce.name = 'Bruce Wayne'
bruce.weight = 85
bruce.height = 185
bruce.alias = 'Batman'
bruce.gender = 'm'
print(bruce.name)
print(bruce.gender)
print(bruce.height)
print(bruce.weight)
print(bruce.hands)
print(bruce.alias)

```
#### Атрибуты и методы классов
```python3
# Магический метод
print(bruce.__dict__)  # Этот магический метод содержит словарь со всеми изменениями, которые были сделаны с атрибутом.
# То, что не менялось, содержится в Person().
print(dir(peter))  # Здесь все методы

# Создаем методы
# self должен быть обязательно в начале!!!!!!!


def eat(self, food):
    self.weight += food


def do_exercise(self, hours):
    self.weight -= hours * 0.2


def change_alias(self, new_alias):
    # print(self)  # Просто смотрим, для чего тут self
    self.alias = new_alias


bruce = Character()
bruce.name = 'Bruce Wayne'
bruce.weight = 85
bruce.height = 185
bruce.gender = 'm'
change_alias(bruce, "Boy")
print(bruce.alias)
do_exercise(bruce, 1)
print(bruce.weight)


class Character:  # Пересоздали класс
    # Создали атрибуты:
    gender = ''
    name = ''
    height = 0
    weight = 0
    hands = 2
    weapons = []  # Добавляем атрибут с изменяемым типом - списком. иначе у всех будет меняться это значение!


peter = Character()
bruce = Character()
print(peter.weapons)
print(bruce.weapons)
peter.weapons.append('web.shooters')
print(peter.weapons)
print(bruce.weapons)
peter.weapons = "1"
print(peter.weapons)
print(bruce.weapons)

```
#### Инициализация класса
````python3
class Character:
    def __init__(self, name, gender, height=0, weight=0, hands=2):
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.hands = hands
        self.weapon = []  # Параметром по умолчанию не будет. Он для конкретного экземпляра.

    def eat(self, food):
        self.weight += food

    def do_exercise(self, hours):
        self.weight -= hours * 0.2

    def change_alias(self, new_alias):
        # print(self)  # Просто смотрим, для чего тут self
        self.alias = new_alias


peter = Character("Peter", "m", height=175)  # name, gender - обязательные!
bruce = Character("Bruce Wayne", "m")
print(peter.height)
print(bruce. hands)
print(peter.__dict__)  # Все атрибуты попали в словарь из-за __init__

num_1 = 5
num_2 = 10
print(num_1 + num_2)
num_1.__add__(num_2)  # Это то же самое, что и num_1 + num_2. (__add__ = +)


def beat_up(self, foe):  # foe - враг
    if not isinstance(foe, Character):  # Проверяем, является ли враг представителем класса Character.
        return
    foe.status = "defeated"  # У врага присваивается статус defeated
    self.status = "winner"  # У персонажа winner


beat_up(bruce, peter)
print(bruce.status)
print(peter.status)

````

## Домашняя работа
#### 
```python3


```