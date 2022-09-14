# 1 задача Арифметика действительных чисел. Вычисления по формулам

# 9, Три сопротивления R u R 2y R 3 соединены параллельно. Найти сопротивление соединения.
#
firstRes = int(input("Введите значение R1: "))
secondRes = int(input("Введите значение R2: "))
thirdRes = int(input("Введите значение R3: "))

result = (firstRes * secondRes * thirdRes) / ((firstRes * secondRes) + (secondRes * thirdRes) + (firstRes * thirdRes))

print('Общее сопротивление при параллельном соединении: ', result, ' Ом')


# 2 задача  Разветвления

# 41, Даны три действительных числа. Выбрать из них
# те, которые принадлежат интервалу ( 1, 3).

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

print('Проверка чисел на наличие в интервале от 1 до 3 \n')

def checkNumber(num):
    if (num < 1 or num > 3):
        print("Число ", num, " не входит в интервал")
    else:
        print("Число ", num, " входит в интервал")


checkNumber(a)
checkNumber(b)
checkNumber(c)

# 3 задача Простейшие циклы

# Даны действительные числа a, h, натуральное число n.
# Вычислить f(a)+2f(а+h)+2f(а+2h)+...+2f(a+(n—1)h)+f(a+nh), где
# f(x) = (x^2 + 1) cos^2 x.

import math

finalValue = int(0)
a = int(input('Введите значение числа а: '))
h = int(input('Введите значение числа h: '))
n = int(input('Введите количество итераций: '))

def base_func(param):
    result = ((param * param + 1) * math.cos(param) * math.cos(param))
    return result

def calc_value(a, h, n, final_val):
    for i in range(n):
        final_val += base_func(a + n * h)
        print(final_val)
    return final_val

print('Результат вычислений: ', calc_value(a, h, n, finalValue))