import re
import math


def numberPtotect(str):
    while 1:
        string = input(f"{str}\n")
        if (re.fullmatch('\s{0,}[-+]?\d{0,}[.]?\d{0,}', string)):
            break
        return float(string)
    

while 1:
    a = 0
    while  (a == numberPtotect("Введтие a")<=0):
        pass
   
    b = numberPtotect("Введтие b")
    c = numberPtotect("Введтие с")

    discriminant = b**2 - (4* a * c)

# b в 2 - 4 ас 