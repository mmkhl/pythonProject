# Число 179 записали 50 раз подряд. Полученное 150-значное число возвели в квадрат. Сколько получилось?

num = str(179)
n = 50
finalNum = ""

for i in range(n):
    finalNum += num
squareNum = int(finalNum) * int(finalNum)
print("Квадрат числа 179 записанного 50 раз подряд: \n", squareNum)

