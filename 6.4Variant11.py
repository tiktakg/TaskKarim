n = int(input("Введите n размера матрицы :\n"))
m = int(input("Введите m размера матрицы :\n"))
matrix,minElement,sumSecondColumn,negativeElement = [],0,0,0

import math 
for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(((math.cos(2) / math.sin(2)) * i)- math.sqrt(3 * j*2))
        if(matrix[i][j] < 0 ):
            negativeElement *= matrix[i][j]

        if(j == 2):
            sumSecondColumn += float(matrix[i][j])
        
        if(i == 3):
            if(j == 0):
                minElement = j
            elif(matrix[i][minElement] > matrix[i][j]):
                minElement = j
       
        

fileOutput = open("filesOutput/fileOutput6.4.txt", "w", encoding='utf-8')

fileOutput.write("Сумма элементов второго столбца" + str(sumSecondColumn) + "\n")
fileOutput.write("Минимальный элемент 3 строки " + str(matrix[3][minElement]) + "\n")
fileOutput.write("Произведение отрицательных элементов матрицы B " + str(negativeElement) + "\n")
fileOutput.write("Вся матрица \n ")
for i in range(n):
    fileOutput.write(str(matrix[i]) + "\n")
    
fileOutput.close()

