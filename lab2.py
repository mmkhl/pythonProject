# Число 179 записали 50 раз подряд. Полученное 150-значное число возвели в квадрат. Сколько получилось?

# num = str(179)
# n = 50
# finalNum = ""
#
# for i in range(n):
#     finalNum += num
# squareNum = int(finalNum) * int(finalNum)
# print("Квадрат числа 179 записанного 50 раз подряд: \n", squareNum)

# Дано натуральное число. Найдите число десятков в его десятичной записи.
# Входные данные
# Вводится единственное число (гарантируется, что число не превышает 10^6).

# import math
# num = int(input("Введите число больше 100: "))
# result = 0
# if num < 100 or num > pow(10, 6):
#     print("Вы ввели число меньше 100")
# else:
#     hundreds = num / 10
#     result = hundreds % 10
#     print("Количество десятков в числе", num, "составляет: ", int(result))


# Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски, определите,
# может ли ладья попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для
# первой клетки, потом для второй клетки.

# a = 8
# mas = [0] * a
# for i in range(a):
#     mas[i] = [0] * a
# print("Расстановка шахматной ладьи\n")
#
# vertFirst = int(input("Введите начальное значение положения для ладьи по вертикали: "))
# horizFirst = int(input("Введите начальное значение положения для ладьи по горизонтали: "))
# vertSecond = int(input("Введите конечное значение положения для ладьи по вертикали: "))
# horizSecond = int(input("Введите конечное значение положения для ладьи по горизонтали: "))
#
# if vertSecond != vertFirst or horizFirst != horizSecond:
#     print("\n Шахматная доска с 2 ладьями\n")
#     mas[vertFirst - 1][horizFirst-1] = 1
#     mas[vertSecond-1][horizSecond-1] = 2
#     for i in range(0, len(mas)):
#         for i2 in range(0, len(mas[i])):
#             print(mas[i][i2], end='  ')
#         print()
# else:
#     raise AttributeError("\nТакого хода быть не может!!!!")
# if vertSecond == vertFirst or horizFirst == horizSecond:
#     print("\nЛадья может попасть в эту клетку!")
# else:
#     print("\nУвы, за один ход так не получится")


# Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n флагов. Изображение одного флага имеет
# размер 4×4 символов, между двумя соседними флагами также имеется пустой (из пробелов) столбец. Разрешается вывести
# пустой столбец после последнего флага. Внутри каждого флага должен быть записан его номер — число от 1 до n.

# n = int(input("Введите количество флагов: "))
# if n <= 9 or n > 0:
#     for i in range(n):
#         print("+___", end=" ")
#     print()
#     for i in range(n):
#         print("|%s /" % (i + 1), end=" ")
#     print()
#     for i in range(n):
#         print("|__\\", end=" ")
#     print()
#     for i in range(n):
#         print("|   ", end=" ")
#     print()


# Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада через год.
# Вклад составляет X рублей Y копеек. Определите размер вклада через K лет.
#
# Входные данные
# Программа получает на вход целые числа P, X, Y, K.
#
# Выходные данные
# Программа должна вывести два числа: величину вклада через K лет в рублях и копейках. Дробное число копеек по
# истечение года отбрасывается. Перерасчет суммы вклада (с отбрасыванием дробных частей копеек) происходит ежегодно.













# Дана строка, в которой буква h встречается как минимум два раза. Повторите последовательность символов,
# заключенную между первым и последнием появлением буквы h два раза, сами буквы h повторять не надо.
#
# Входные данные
# Вводится строка.













# Определите сумму всех элементов последовательности, завершающейся числом 0.
# Входные данные
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит,
# а служит как признак ее окончания).
