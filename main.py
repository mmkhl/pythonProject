# 1 задача Арифметика действительных чисел. Вычисления по формулам

# 9, Три сопротивления R u R 2y R 3 соединены параллельно. Найти сопротивление соединения.

# firstRes = int(input("Введите значение R1: "))
# secondRes = int(input("Введите значение R2: "))
# thirdRes = int(input("Введите значение R3: "))
#
# result = (firstRes * secondRes * thirdRes) / ((firstRes * secondRes) + (secondRes * thirdRes) + (firstRes * thirdRes))
#
# print('Общее сопротивление при параллельном соединении: ', result, ' Ом')


# 2 задача  Разветвления

# 41, Даны три действительных числа. Выбрать из них
#те, которые принадлежат интервалу ( 1, 3).

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

print('Проверка чисел на наличие в интервале от 1 до 3 \n')

def checkNumber (num):
    if (num < 1 or num > 3):
        print("Число ", num, " не входит в интервал")
    else:
        print("Число ", num, " входит в интервал")

checkNumber(a)
checkNumber(b)
checkNumber(c)


# 3 задача Простейшие циклы

# Даны действительные числа а, Л, натуральное число я.
# Вычислить f (a) + 2/ (а + h) + 2/ (а + 2h) + ... + -2f(a + (n— l)h) + f(a + nh), где
# f(x) = (x^2 + 1) cos^2 x.

