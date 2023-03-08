import math
k = float(input("Введите k \n"))

a, z = -1, 0


while 1:
    try:
        z += (math.log(math.fabs((math.cos(a**2) / math.sin(a**2))) - k*1)) / (k*2*-a)
        print(z)
    except:
        pass

    a += 0.3
    if (a >= 6):
        break


fileOutput = open("filesOutput/fileOutput4.4.txt", "w")
fileOutput.write(str(z))
fileOutput.close()
