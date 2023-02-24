m = int(input("Введите количество членов ряда m \n"))
x = int(input("Введите x \n"))

c = 0

from math import cos

for n in range(0,m):
    print((cos(2)*n*x ) / pow((2*n+1),2))
    c += (cos(2)*n*x ) / pow((2*n+1),2)

fileOutput = open("fileOutput4.2.txt","w")
fileOutput.write(str(c))
fileOutput.close()