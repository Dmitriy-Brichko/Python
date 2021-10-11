courses_list = [
    {'title': 'Java разработчик с нуля',
     'mentors': ['Павел Дерендяев', 'Алексей Яковлев', 'Сергей Сердюков'], 'duration': 11},
    {'title': 'Веб-разработчик с нуля', 'mentors': ['Николай Лопин', 'Алена Батицкая', 'Алексей Дацков',
                                                    'Александр Беспоясов'], 'duration': 18},
    {'title': 'Fronted разработчик с нуля', 'mentors': ['Ильназ Гилязов', 'Татьяна Тен', 'Алена Батицкая',
                                                        'Александр Фитискин', 'Владимир Чебукин', 'Эдгард Нурулин'],
     'duration': 13}
]

# for course in courses_list:
#     print('Название курса: {}'.format(course['title']))
#     print('Преподаватели: {}'.format(", ".join(course['mentors'])))
#     print()

# for course in courses_list:
#     for k, v in course.items():
#         print(f"Ключ = {k}, значение = {v}")

# max_count = 0
# leader_id = -1
# for id, course in enumerate(courses_list):
#     print('Название курса: {}'.format(course['title']))
#     count = len(course['mentors'])
#     print(f'Количество преподавателей: {count}')
#     if count > max_count:
#         max_count = count
#         leader_id = id
# print("Наш лидер - курс {}, преподавателей: {}".format(courses_list[id]['title'], len(courses_list[id]['mentors'])))

# new_course_dict = {}
# new_course_dict.setdefault('title', 'C++')
# new_course_dict.setdefault('mentors', ['123'])
# if 'mentors' not in new_course_dict.keys():  # !!! 1) Если нет ключа,
#     new_course_dict['mentors'] = []  # !!! то это его создаст
# key = new_course_dict.get('mentors')  # ??? 2) Еще можно так
# if key is None:  # ??? создать ключ
#     new_course_dict['mentors'] = []  # ???
# new_course_dict.setdefault('mentors', [])  # %%% 3) А лучше так
# new_course_dict.setdefault('mentors', ['это значение он не запишет, т.к. это команда безопасная и не перезаписывает'
#                                        ' то, что уже есть'])
# new_course_dict['mentors'].append('Олег Булыгин')  # Эта строка добавит строку Олега в список
# # new_course_dict['mentors'] = ['Олег Булыгин']  # А эта строка перезаписывает, т.к. без .setdefault
# new_course_dict.setdefault('duration', 15)
# print(new_course_dict)

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

