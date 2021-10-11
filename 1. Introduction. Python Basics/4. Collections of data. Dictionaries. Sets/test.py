telephones_dict = dict()  # Создать словарь
capitals_dict = {'Russia': 'Moscow', 'Ukraine': 'Kiev'}  # Создать словарь
dict_1 = {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
print(dict_1)
print(capitals_dict['Russia'])
# Итерация по словарю:
for country, capital in capitals_dict.items():
    print(country, '->', capital)
# Добавление нового элемента в словарь:
capitals_dict['France'] = 'Paris'

