n = int(input("Введите n размера матрицы :\n"))
m = int(input("Введите m размера матрицы :\n"))

import numpy
import random

matrix = [[round(random.uniform(-6, 7),3)  for x in range(n)] for y in range(m)]

import pprint
pprint.pprint(matrix)