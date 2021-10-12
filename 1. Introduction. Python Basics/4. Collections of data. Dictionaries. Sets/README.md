## Работа на лекции
##### Словари
```python3
# key:value
# Все ключи уникальные!
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

```
#### Операции со словарями
```python3
del(dict[key])  # Удалить элемент из списка по ключу
.keys()  # Позволяет получить все ключи словаря 
.values()  # Позволяет получить все значения словаря
.items()  # Позволяет получить все ключи и значения словаря
.get(key)  # "Безопасно" возвращает значение по ключу (при отсутствии ключа ошибка не возникает)
.setdefault(key, default)  # Позволяет получить значение по ключу, автоматически побавляет элемент в словарь, 
# если его нет.

```
#### Множества
```python3
set()
frozenset  # Неизменяемое множество
```
#### Операции над множествами
```python3
.add(el)  # Добавляет элемент в множество
.update(set)  # Соединяет множество с другим множеством/списком
.diskard(el)  # удаляет элемент из множества по его значению
.union(set)  # Объединяет множество (логическое ИЛИ)
.intersection(set)  # Пересечение множеств (логическое И)
.difference(set)  # Возвращяет элементы одного множества, которые не принадлежат другому множеству (разность множеств)
.symmetric_difference(set) # Возвращяет элементы, которые встречаются в одном множестве, но не встречаются в обоих.

```
```Python3
courses_list = [
    {'title': 'Java разработчик с нуля',
     'mentors': ['Павел Дерендяев', 'Алексей Яковлев', 'Сергей Сердюков'], 'duration': 11},
    {'title': 'Веб-разработчик с нуля', 'mentors': ['Николай Лопин', 'Алена Батицкая', 'Алексей Дацков',
                                                    'Александр Беспоясов'], 'duration': 18},
    {'title': 'Fronted разработчик с нуля', 'mentors': ['Ильназ Гилязов', 'Татьяна Тен', 'Алена Батицкая',
                                                        'Александр Фитискин', 'Владимир Чебукин', 'Эдгард Нурулин'],
     'duration': 13}
]

for course in courses_list:
    print('Название курса: {}'.format(course['title']))
    print('Преподаватели: {}'.format(", ".join(course['mentors'])))
    print()

for course in courses_list:
    for k, v in course.items():
        print(f"Ключ = {k}, значение = {v}")

max_count = 0
leader_id = -1
for id, course in enumerate(courses_list):
    print('Название курса: {}'.format(course['title']))
    count = len(course['mentors'])
    print(f'Количество преподавателей: {count}')
    if count > max_count:
        max_count = count
        leader_id = id
print("Наш лидер - курс {}, преподавателей: {}".format(courses_list[id]['title'], len(courses_list[id]['mentors'])))

new_course_dict = {}
new_course_dict.setdefault('title', 'C++')
new_course_dict.setdefault('mentors', ['123'])
if 'mentors' not in new_course_dict.keys():  # !!! 1) Если нет ключа,
    new_course_dict['mentors'] = []  # !!! то это его создаст
key = new_course_dict.get('mentors')  # ??? 2) Еще можно так
if key is None:  # ??? создать ключ
    new_course_dict['mentors'] = []  # ???
new_course_dict.setdefault('mentors', [])  # %%% 3) А лучше так
new_course_dict.setdefault('mentors', ['это значение он не запишет, т.к. это команда безопасная и не перезаписывает'
                                       ' то, что уже есть'])
new_course_dict['mentors'].append('Олег Булыгин')  # Эта строка добавит строку Олега в список
new_course_dict['mentors'] = ['Олег Булыгин']  # А эта строка перезаписывает, т.к. без .setdefault
new_course_dict.setdefault('duration', 15)
print(new_course_dict)

java_set = set(courses_list[0]['mentors'])
web_set = set(courses_list[1]['mentors'])
fronted_set = set(courses_list[2]['mentors'])
print(f"{type(java_set)}, {java_set}")

# Пересечение
print(f"Java & Web: {java_set & web_set}")
print(f"Java & Fronted: {java_set & fronted_set}")
print(f"Fronted & Web: {fronted_set & web_set}")

# Объединение
print(f"Java & Web: {java_set | web_set}")

# Разность (те, кто точно не преподает на Web)
print(f"Разность Fronted и Web {fronted_set - web_set}")
# Разность (те, кто точно не преподает на Fronted)
print(f"Разность Web и Fronted {web_set.difference(fronted_set)}")
# Симетрическая разность (здесь нет того, кто есть и там и там)
print(f"Симетрическая разность Fronted и Web {fronted_set ^ web_set}")
print(f"Симетрическая разность Web и Fronted {web_set.symmetric_difference(fronted_set)}")

```
## Домашняя работа
### Задача №1
#### Дан список с визитами по городам и странам. Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России."
```python3
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
geo_logs_russia = []

for geo in geo_logs:
    for key, value in geo.items():
        if 'Россия' in value:
            print(f"{key} ! {value}")
            geo_logs_russia.append({key: value})

print(geo_logs_russia)

```
### Задача №2
#### Выведите на экран все уникальные гео-ID из значений словаря ids. Т.е. список вида [213, 15, 54, 119, 98, 35]

