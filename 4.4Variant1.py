k = float(input("Введите k \n"))

a,z= -1,0


import math

while 1:
    z += (math.cos(math.fabs(a**2) - k*1)) / (k*2*-a )
    print(z)
    a+= 0.3
    if(a >=6):
        break


fileOutput = open("fileOutput4.4.txt","w")
fileOutput.write(str(z))
fileOutput.close()