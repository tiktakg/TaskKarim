import random
import numpy as np

sumElementDiagonal, sumElemenUpMainDiagonal, minElementThrirdStr = 0.0, 0.0, 0.0,

n = int(input("Введите n размера матрицы :\n"))
m = int(input("Введите m размера матрицы :\n"))


matrix= np.array([[round(random.uniform(-6, 7), 3) for x in range(n)]
          for y in range(m)])


for i in range(n):
    for j in range(m):
        if (i == j):
            sumElementDiagonal += float(matrix[i][j])
        elif (i+j == n - 1):
            sumElementDiagonal += float(matrix[i][j])
        if (i > j):
            sumElemenUpMainDiagonal += float(matrix[i][j])
        if(i == 3):
            testMin = matrix[i][j]
            if(minElementThrirdStr > testMin):
               minElementThrirdStr = testMin


fileOutput = open("filesOutput/fileOutput7.1.txt", "w", encoding='utf-8')
fileOutput.write("Минимальный элемент третей строки " + str(print(minElementThrirdStr)) + "\n")
fileOutput.write("Сумма элементов выше гланой диагонали" + str(sumElemenUpMainDiagonal) + "\n")
fileOutput.write("Сумма элементов гланой диагонали" + str(sumElementDiagonal) + "\n")
fileOutput.write("Ранг матрицы" + str(np.linalg.matrix_rank(matrix)) + "\n")


fileOutput.write("Вся матрица \n ")
for i in range(n):
    fileOutput.write(str(matrix[i]) + "\n")

fileOutput.write("Вся матрица M1 созданная на основе первой строки и умноженная на исходную матрицу \n ")
M1 = np.diag(matrix[0])
result = matrix * M1

for i in range(n):
    fileOutput.write(str(result[i]) + "\n")

fileOutput.close()

