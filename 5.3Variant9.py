ru = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
eu = set('abcdefghijklmopqustwxyzABCDEFGHIJKLMOPQUSTWXYZ')

euVowels = 'bcdfghjklmnpqrstvwxz'

isNumber,isUpper,isLower,isRu,isEu, = False,False,False,False,False

countLetters = 0

file = open('fileInput5.2.txt')
str = file.read()
    
if(len(str) < 20):
    if any(char.isdigit() for char in str):
        isNumber = True
    if any(char.isupper() for char in str):
        isUpper = True
    if any(char.lower() for char in str):
        isLower = True
    if(ru.intersection(str) != set()):
        isRu = True
    if(eu.intersection(str) != set()):
        isEu =True
    if(isLower and isUpper and isNumber and isRu and isEu):
           print("Файле подходит")
else:
    print("Файле меньше 20 символов")

for i in range(len(str)):
    for j in range(len(euVowels)):
        if(str[i] == euVowels[j]):
            countLetters +=1
            

strForWrite = "Количество согласных строчных латинских букв " +  str(countLetters)
fileOutput = open("fileOutput5.3.txt","w")
fileOutput.write(strForWrite)
fileOutput.close()