from grade.decorators import weight


class Animals:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food = 50
        self.i += 1!!!!!!!!!!!!!


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


if __name__ == '__main__':
    print(__name__)
# print(Animals(object))
# for i in Animals.weight:
#     print(i)

