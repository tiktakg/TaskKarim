x = int(input("Введите x \n"))
y = int(input("Введите y \n"))

from math import sin 

if(x > 5 and 4 < y <5):
    f = 6 * x + 2*y
elif(0 < x <=5 or y <=5):
    f = 3-x*y
else:
    f = sin(3) * x

print(f)