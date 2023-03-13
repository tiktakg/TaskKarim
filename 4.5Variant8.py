import math  
x,n,Sn = 0.0,0,0.0

while 1:
    x = float(input("Введите x которое больше 0 но меньше 2\n"))
    if (x >= 0 and x <= 2) :
        break

while 1:
    Sn +=float(((-1)**n)*(((2*x-5)*math.log(3)**n)/ float(math.factorial(n))))

    if(Sn >= 3**(2*x-5)):
        break

    n+=1

fileOutput = open("filesOutput/fileOutput4.5.txt", "w")
fileOutput.write(str(Sn))
fileOutput.close()