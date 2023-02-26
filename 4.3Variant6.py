k = float(input("Введите k \n"))

z,y= -1,0


import math

while z <= 6:
    y += (math.sqrt(k*1+z) - k*2) / (k*2*math.atan(0.1)*z )
    print(y)
    z+= 0.4


fileOutput = open("fileOutput4.3.txt","w")
fileOutput.write(str(y))
fileOutput.close()