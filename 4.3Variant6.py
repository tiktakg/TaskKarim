k = int(input("Введите k \n"))

z,y= -1,0


import math

while z <= 6:
    print((math.sqrt(k*1+z) - k*2))
    print((k*2*math.atan(0.1)*z ))
    y += (math.sqrt(k*1+z) - k*2) / (k*2*math.atan(0.1)*z )
    print(y)
    z+= 0.5


fileOutput = open("fileOutput4.3.txt","w")
fileOutput.write(str(y))
fileOutput.close()