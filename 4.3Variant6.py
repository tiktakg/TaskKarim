import math
k = float(input("Введите k \n"))

z, y = -1, 0


while z <= 6:
    if (z == 0):
        z += 0.5
        continue

    y += (math.sqrt(k*1+z) - k*2) / (k*2*math.atan(0.1)*z)
    print(y)
    z += 0.5


fileOutput = open("filesOutput/fileOutput4.3.txt", "w")
fileOutput.write(str(y))
fileOutput.close()
