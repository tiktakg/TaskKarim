M, N, MN1, MN2 = [], [], [], []

for i in range(7):
    M.append(int(input("Введите число массива C\n")))

    if (i < 5):
        N.append(int(input("Введите число массива N\n")))


fileOutput = open("filesOutput/fileOutput6.3.txt", "w", encoding='utf-8')
fileOutput.write("Исскходный массив M " + str(M) + "\n")
fileOutput.write("Иссходный массив N " + str(N) + "\n")

del M[3]
N.append(44)
N[2] = 22
MN1 = sorted(M + N)

fileOutput.write("Полученный массив, M c удаленным 3 элементом " + str(M) + "\n")
fileOutput.write("Полученный массив, N c добовлениеем 44 в конец и 22 на второе место " + str(N) + "\n")
fileOutput.write("Полученный массив MN1, отсортированный по возростнаию " + str(MN1) + "\n")
fileOutput.write("Позиция элемента 22 в массиве MN1 " + str(MN1.index(22)) + "\n")



MN2 = [0 for i in range(len(MN1)*2)]
MN3 =  [0 for i in range(len(MN2)+2)]

i, j = 0, 0
while 1:
    if ((i % 2) != 0):
        MN2[i] = MN1[j]
        j += 1
    else:
        MN2[i] = 0
    i += 1

    if (i == len(MN1)*2):
        break



fileOutput.write("Полученный массив MN2, с записаными в нечетные позиции элементами" + str(MN2) + "\n")


for i in range(len(MN2)- 2):
        MN3[i] = MN2[i + 2]

MN3[len(MN2)] = MN2[1]
MN2 = MN3


fileOutput.write("Полученный массив MN2, с записаными в нечетные позиции элементами, и со сдвигом на 2 влево" + str(MN2) + "\n")
fileOutput.close()
