n = int(input("Введите n размера матрицы :\n"))
m = int(input("Введите m размера матрицы :\n"))
matrix,minElement,sumSecondColumn,negativeElement = [],0,0,0

import math 
for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(((math.cos(2) / math.sin(2)) * i)- math.sqrt(3 * j*2))
        negativeElement *= matrix[i][j]
        if(j == 2):
            sumSecondColumn += float(matrix[i][j])
        
        if(i == 3):
            if(j == 0):
                minElement = j
            elif(matrix[i][minElement] > matrix[i][j]):
                minElement = j
       
        

print(matrix[3][minElement])
print(sumSecondColumn)

for i in range(n):
    print(matrix[i])

