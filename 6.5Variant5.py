file = open('fileInput6.5.txt')
strings,columns, sumLastColumn,sumElementDiagonal,matrix = 0,0, 0.0,0,[]
sumCol,maxCol,indx = 0,0,0

for line in file:
    row = line.split()
    matrix.append([])
    matrix[strings] = list(map(float, row))
    sumLastColumn += float(row[len(row)-1])
    sumElementDiagonal +=float(row[len(row)-(strings+1)])
    strings += 1
    columns = len(row)

file.close()


for i in range(strings):
    sumCol = sum(matrix[j][i] for j in range(columns))
    if(maxCol < sumCol):
        maxCol =sumCol
        indx = 1


fileOutput = open("filesOutput/fileOutput6.5.txt", "w", encoding='utf-8')
fileOutput.write("Сумма элементов побочной диагонали и разделенная на сумму всех элементов последнего столбца " + str(sumElementDiagonal / sumLastColumn) + "\n")
fileOutput.write("Столбец с максильной суммой элементов " + str(indx) + "\n")

fileOutput.write("Вся матрица \n ")
for i in range(strings):
    fileOutput.write(str(matrix[i]) + "\n")

fileOutput.close()
