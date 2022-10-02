# Дано натуральное число n>1. Выведите его наименьший делитель, отличный от 1.
# Решение оформите в виде функции MinDivisor(n). Алгоритм должен иметь сложность O(n√).
# Указание. Если у числа n нет делителя не превосходящего n−−√, то число n — простое и ответом будет само число n.
#
num = int(input("Введите число, отличное от нуля: "))

def MinDivisor(n):
    if n <= 1:
        print("Введенное число должно быть больше единицы!")
    else:
        if n % n ** 0.5 == 0:
            return int(n ** 0.5)
        else:
            return n

print("Результат: ", MinDivisor(num))

# Выведите значение наименьшего нечетного элемента списка, а если в списке нет нечетных элементов - выведите число 0.
# Входные данные
# Вводится список чисел. Все числа списка находятся на одной строке.

someNumList = list(map(int, input().split()))
defaultMin = 0
def checkMin(num):
    global defaultMin
    for i in range(len(num)):
        if num[i] % 2 == 1:
            defaultMin = num[i]
            break
    for i in range(len(num)):
        if num[i] % 2 == 1:
            if num[i] < defaultMin:
                defaultMin = num[i]
    if defaultMin != 0:
        print(defaultMin)
    else:
        print(0)
    return defaultMin
print("Минимальное значение: ", checkMin(someNumList))

# A: Четные индексы
# Решите эту задачу в одну строку

print(" ".join(input().split()[::2]))
