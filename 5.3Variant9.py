ru = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
eu = set('abcdefghijklmopqustwxyzABCDEFGHIJKLMOPQUSTWXYZ')

euVowels = 'bcdfghjklmnpqrstvwxz'

isNumber,isUpper,isLower,isRu,isEu, = False,False,False,False,False

countLetters = 0

file = open('fileInput5.3.txt')
string = file.read()
    
if(len(string) < 20):
    if any(char.isdigit() for char in string):
        isNumber = True
    if any(char.isupper() for char in string):
        isUpper = True
    if any(char.lower() for char in string):
        isLower = True
    if(ru.intersection(string) != set()):
        isRu = True
    if(eu.intersection(string) != set()):
        isEu =True
    if(isLower and isUpper and isNumber and isRu and isEu):
           print("Файле подходит")
else:
    print("Файле меньше 20 символов")

for i in range(len(string)):
    for j in range(len(euVowels)):
        if(string[i] == euVowels[j]):
            countLetters +=1
            


fileOutput = open("filesOutput/fileOutput5.3.txt","w", encoding='utf-8')
fileOutput.write("Количество согласных строчных латинских букв " +  str(countLetters))
fileOutput.close()