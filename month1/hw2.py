day = int(input('Введите день: '))
month = int(input('Введите месяц: '))

if (month == 3 and 21 <= day <= 31) or (month == 4 and 1 <= day <= 20):
    print("Овен")
elif (month == 4 and 21 <= day <= 30) or (month == 5 and 1 <= day <= 21):
    print('Телец')
elif (month == 5 and 22 <= day <= 31) or (month == 6 and 1 <= day <= 21):
    print('Близнецы')
elif (month == 6 and 22 <= day <= 30) or (month == 7 and 1 <= day <= 22):
    print('Рак')
elif (month == 7 and 23 <= day <= 31) or (month == 8 and 1 <= day <= 21):
    print('Лев')
elif (month == 8 and 22 <= day <= 31) or (month == 9 and 1 <= day <= 23):
    print('Дева')
elif (month == 9 and 24 <= day <= 30) or (month == 10 and 1 <= day <= 23):
    print('Весы')
elif (month == 10 and 24 <= day <= 31) or (month == 11 and 1 <= day <= 22):
    print('Скорпион')
elif (month == 11 and 23 <= day <= 30) or (month == 12 and 1 <= day <= 22):
    print('Стрелец')
elif (month == 12 and 23 <= day <= 31) or (month == 1 and 1 <= day <= 20):
    print('Козерог')
elif (month == 1 and 21 <= day <= 31) or (month == 2 and 1 <= day <= 19):
    print('Водолей')
elif (month == 2 and 20 <= day <= 29) or (month == 3 and 1 <= day <= 20):
    print('Рыбы')
else:
    print('Ошибка: введены некорректные данные')
