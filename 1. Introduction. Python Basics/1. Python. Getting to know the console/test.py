import time


try:
    wages = float(input('Укажите Вашу заработную плату в месяц в рублях. :'))
except ValueError:
    print('Введено не число!!!')
    print('Значение вводится целым или десятичным цислом!')
    wages = float(input('Укажите Вашу заработную плату в месяц в рублях. :'))

try:
    percent_from_wages_for_mortgage = float(input('Какой процент(%) от зп у Вас уходит на себя? :'))
except ValueError:
    print('Введено не число!!!')
    print('Значение вводится целым или десятичным цислом!')
    percent_from_wages_for_mortgage = input('Какой процент(%) от зп у Вас уходит на себя? :')

try:
    percent_from_wages_for_live = float(input('Какой процент(%) от зп у Вас уходит "на жизнь"? :'))
except ValueError:
    print('Введено не число!!!')
    print('Значение вводится целым или десятичным цислом!')
    percent_from_wages_for_live = input('Какой процент(%) от зп у Вас уходит "на жизнь"? :')

money_for_mortgage = float(wages) * float(percent_from_wages_for_mortgage) / 100.0
money_for_mortgage_in_year = float(money_for_mortgage * 12.0)
money_for_live = float(wages) * float(percent_from_wages_for_live) / 100.0
savings_money_for_month = float(wages) - float(money_for_mortgage) - float(money_for_live)
savings_money_for_year = float(savings_money_for_month) * 12.0
print('Потрачено денег в год на себя' ,money_for_mortgage_in_year, 'р.')
print('Накоплено денег за год', savings_money_for_year, 'р.')
time.sleep(900000)
