try:
    lehgth_a = float(input('Введите длину прямоугольника :'))
    lehgth_b = float(input('Введите ширину прямоугольника :'))
    print(float(lehgth_a) * float(lehgth_b))
except ValueError:
    print('Введено не число')
    print('Длина вводится целым или десятичным цислом!')
    lehgth_a = float(input('Введите длину прямоугольника :'))
    lehgth_b = float(input('Введите ширину прямоугольника :'))
    print(float(lehgth_a) * float(lehgth_b))