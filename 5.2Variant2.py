file = open('fileInput5.2.txt')
str = file.read()

isNumber,isUpper,isLower = False,False,False

if(len(str) < 20):
    if any(char.isdigit() for char in str):
            isNumber = True
    if any(char.isupper() for char in str):
            isUpper = True
    if any(char.lower() for char in str):
            isLower = True
    if(isLower and isUpper and isNumber):
        print("Файле подходит")
else:
    print("Файле меньше 20 символов")

        


strWithDouble = ""
for char in str:
    if(char.isalpha()):
        strWithDouble +=char + char
    else:
        strWithDouble +=char

fileOutput = open("fileOutput5.2.txt","w")
fileOutput.write(strWithDouble)
fileOutput.close()





  
  