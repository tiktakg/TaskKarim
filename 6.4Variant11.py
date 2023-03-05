n = int(input("Введите n размера матрицы :\n"))
m = int(input("Введите m размера матрицы :\n"))
matrix,minElement,sumSecondColumn = [],0,0

import math 
for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(((math.cos(2) / math.sin(2)) * i)- math.sqrt(3 * j*2))
    
    if(i == 1):
        print(matrix[1][i])
        sumSecondColumn += matrix[1][i]
       
        

print(matrix[1][1])

print(sumSecondColumn)

for i in range(n):
    print(matrix[i])

