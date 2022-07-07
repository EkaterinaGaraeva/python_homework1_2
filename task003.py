# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# *Пример:*
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def checking(number):
    result = True
    for i in number:
        if i not in '1234567890.-':
            result = False
    return result

def quarter_number(x, y):
    while (checking(x) != True):
        x = input('Введите координату точки X: ')
    else:
        x = float(x)
    while (checking(y) != True):
        y = input('Введите координату точки Y: ')
    else:
        y = float(y)
    if x > 0 and y > 0:
        print('Точка находится в I четверти')
    elif x < 0 and y > 0:
        print('Точка находится во II четверти')
    elif x < 0 and y < 0:
        print('Точка находится в III четверти')
    elif x > 0 and y < 0:
        print('Точка находится в IV четверти')
    elif (x == 0) and (y == 0):
        print('Точка находится в начале координат')
    elif (x == 0):
        print('Точка находится на оси X')
    elif (y == 0):
        print('Точка находится на оси Y')

x = input('Введите координату точки X: ')
y = input('Введите координату точки Y: ')
quarter_number(x, y)