professions = ['IT', 'Физика', 'Математика']
persons = [
    ['Гейтс', 'Джобс', 'Возняк'],
    ['Эйнштейн', 'Фейнман'],
    ['Эвклид', 'Ньютон']
    ]
for pro, names in zip(professions, persons):
    print(f'{pro}:')
    for name in names:
        print(name)
    print()
