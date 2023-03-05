B = []
for i in range(8):
    number = float(input("Введите число \n"))
    B.append(number)

x = float(input("Введите x \n"))

sum,positiveElement = 0.0,0

import math   

for i in range(len(B)):
    B[i] = (math.cos(B[i]**2) / math.sin(B[i]**2) ) - x* math.sqrt(2*B[i])

    if(B[i] > 0):
        positiveElement +=1

for i in range(2,len(B),2):
    sum += B[i]


fileOutput = open("filesOutput/fileOutput6.1.txt","w", encoding='utf-8')

fileOutput.write("Полученный массив" + str(B)+ "\n")
fileOutput.write("Cумма элементов с четным индексом " + str(sum) + "\n")
fileOutput.write("Количество положительных элементов " + str(positiveElement)+ "\n")

fileOutput.close()

