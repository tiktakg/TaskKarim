import math
import array as a

A = a.array('f')
b = float(input("Введите b \n"))
minElement, element, positionMinElement = 0, 0, 0

for i in range(10):
    A.append(float(input("Введите число \n")))
    A[i] = 3*math.sqrt(b*A[i]) - math.tan(2) * A[i]

    if (i == 0):
        minElement = A[0]
    element = A[i]

    if (minElement >= A[i]):
        minElement = element
        positionMinElement = i


fileOutput = open("filesOutput/fileOutput6.2.txt", "w", encoding='utf-8')
fileOutput.write("Минимальный элемент \n" + str(minElement) + "\n")
fileOutput.write("Полученный массив \n" + str(' '.join(map(str, A))) + "\n")

A[positionMinElement] = A[9]
A[9] = minElement

fileOutput.write("Минимальный и последний элемент поменяны местами массив \n" + str(' '.join(map(str, A))) + "\n")
fileOutput.close()
