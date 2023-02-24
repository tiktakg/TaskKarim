c = int(input("Введите c \n"))
y = int(input("Введите y \n"))
x = int(input("Введите x \n"))

from math import fabs

h = ((c*y + x*x*(y**5 - 1)) / fabs(c - x - y)) + ((2 * x**3 + 3)/(y -x)**2)

print(h) 
print(round(h))
print(round(h, 1))
print(round(h, 2))