import re
import math

def numberPtotect(str):
    string = ""
    while 1:
        string = input(f"{str}\n")
        if (re.fullmatch('\s{0,}[-+]?\d{0,}[.]?\d{0,}', string)):
            break
    return float(string)
    
x = numberPtotect("Введтие x")
y = numberPtotect("Введтие y")

print(((1+1/x**x)**x) - 12*(x**2)*y )

x = numberPtotect("Введтие x")
e = numberPtotect("Введтие e")

print((e**x) -x-2+((1+x)**x))

