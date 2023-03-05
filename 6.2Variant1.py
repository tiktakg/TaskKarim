import math
import array as a

A = a.array('f')
b = float(input("Введите b \n"))
positionMinElement = 0

for i in range(10):
    A.append(float(input("Введите число \n")))
    A[i] = 3*math.sqrt(b*A[i]) - math.tan(2) * A[i]

    if (i == 0):
        positionMinElement = 0

    if (A[positionMinElement] >= A[i]):
        positionMinElement = i


fileOutput = open("filesOutput/fileOutput6.2.txt", "w", encoding='utf-8')
fileOutput.write("Минимальный элемент \n" + str(A[positionMinElement]) + "\n")
fileOutput.write("Полученный массив \n" + str(' '.join(map(str, A))) + "\n")

A[positionMinElement], A[9]  = A[9],A[positionMinElement]

fileOutput.write("Минимальный и последний элемент поменяны местами массив \n" + str(' '.join(map(str, A))) + "\n")
fileOutput.close()
