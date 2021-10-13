list_1 = ['2018-01-01', 'yandex', 'cpc', 100]
list_2 = {}

for dict_1 in list_1:
    print(dict_1)
    list_2.setdefault(dict_1)

print(list_2)

