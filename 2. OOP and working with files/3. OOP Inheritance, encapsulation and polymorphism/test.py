class Test:
    def __init__(self, gender):
        self.gender = gender
        self.__name = 'Peter Parker'
        self._alias = "No alias"  # этот псевдоним стал protected

    def _change_alias(self, new_alias):  # Метод тоже защищенный
        self._alias = new_alias

    def __change_name(self, name):
        self.__name = name


peter = Test('m')
print(peter._alias)  # Но (_protected) в Python не работает! :D
peter._change_alias('Spider-Man')  # Но (_protected) в Python не работает! :D
print(peter._alias)  # Но (_protected) в Python не работает! :D

# print(peter.__name)  # Нет доступа к атрибуту вне класса
# peter.__change_name('hren')  # Нет доступа к методам вне класса
# print(peter.__name)  # Нет доступа к атрибуту вне класса

# Но это можно обойти!
print(peter._Test__name)
peter._Test__change_name('hren1')
print(peter._Test__name)
