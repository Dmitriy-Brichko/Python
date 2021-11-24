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
Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:

* гусей "Серый" и "Белый"
корову "Маньку"
овец "Барашек" и "Кудрявый"
кур "Ко-Ко" и "Кукареку"
коз "Рога" и "Копыта"
и утку "Кряква"
Со всеми животными вам необходимо как-то взаимодействовать:
* кормить
корову и коз доить
овец стричь
собирать яйца у кур, утки и гусей
различать по голосам(коровы мычат, утки крякают и т.д.)
#### Задача №1
Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с животными и дополнить их в дочерних классах, если потребуется.

#### Задача №2
Для каждого животного из списка должен существовать экземпляр класса. Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.

#### Задача №3
У каждого животного должно быть определено имя(self.name) и вес(self.weight).

Необходимо посчитать общий вес всех животных(экземпляров класса);
Вывести название самого тяжелого животного.
```python3
class Animals:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food = 50


class TakeMilk(Animals):
    milk = 50


class TakeEggs(Animals):
    eggs = 50


class Sheep(Animals):
    trim = 50


class Geese(TakeEggs):
    voice = "Га-Га-Га"


class Cows(TakeMilk):
    voice = "Муууу"


class Chickens(TakeEggs):
    voice = "Кут-кудах"


class Goats(TakeMilk):
    voice = "Бее"


class Ducks(TakeEggs):
    voice = "Кря"


def eat(self, food):
    self.food += food


def collect_eggs(self, eggs):
    self.eggs -= eggs


def milking(self, volume_milk):
    self.milk -= volume_milk


def cut(self, trim):
    self.trim -= trim


goose_gray = Geese("Серый", 10)
goose_white = Geese("Белый", 11)
cow_manyka = Cows("Манька", 80)
ship_barashek = Sheep("Барашек", 40)
ship_kudryaviy = Sheep("Кудрявый", 41)
chicken_koko = Chickens("Ко-Ко", 5)
chicken_kukareku = Chickens("Кукареку", 6)
goat_roga = Goats("Рога", 20)
goat_kopita = Goats("Копыта", 21)
duck_kryakva = Ducks("Кряква", 30)

eat(goose_white, 9)
collect_eggs(goose_gray, 5)
milking(cow_manyka, 11)
cut(ship_barashek, 7)

print(goose_gray.__dict__)
print(goose_white.__dict__)
print(cow_manyka.__dict__)
print(ship_barashek.__dict__)
print(ship_kudryaviy.__dict__)
print(chicken_koko.__dict__)
print(chicken_kukareku.__dict__)
print(goat_roga.__dict__)
print(goat_kopita.__dict__)
print(duck_kryakva.__dict__)
print(goose_white.eggs)
print(goose_white.voice)
print(dir(goose_gray))

test = [goose_gray, goose_white, cow_manyka, ship_barashek, ship_kudryaviy, chicken_koko, chicken_kukareku, goat_roga,
        goat_kopita, duck_kryakva]
all_weight = 0
biggest = 0

for i in test:
    print(i.weight)
    all_weight += i.weight
    if i.weight > biggest:
        biggest = i.weight
        
print(all_weight)
print(biggest)

```