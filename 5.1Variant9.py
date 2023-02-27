file = open('fileInput5.1.txt')
str = file.read()

if(len(str) > 45):
   print("В файле больше 45 символов ")




str = str.replace('a','o')
str = str.replace('а','o')

str = str.replace('А','o')
str = str.replace('A','o')

str = str.capitalize()


fileOutput = open("fileOutput5.1.txt","w", encoding='utf-8')
fileOutput.write(str.ljust(45))
fileOutput.close()

