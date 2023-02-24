a = int(input("Введите a \n"))
b = int(input("Введите b \n"))
c = int(input("Введите c \n"))

if(a < 0 or b < 0 or c < 0):
    print("Одна из переменных отрицательная")
else:
    print("Ни одна из переменных не отрицательная")