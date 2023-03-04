import os
import shutil

def checkfile(str = "", FileName = ""):
    if(str == ""):
        FileName = input("Введите путь к файлу и  название файла \n")
    if(os.path.exists(FileName) or os.path.exists(str)):
        print("Файл существует")
        return FileName
    else:
        print("Файл не существует ")
        return False


def checkDir():
    dirName = input("Введите название каталога \n")

    if(os.path.isdir(dirName)):
        print("Каталог существует")
    else:
        print("Каталог не существует ")

def renameFile():
    fileName = input("Введите название файла которое нужно переминовать \n")
    if(checkfile(fileName) != False):
        fileNameTwo = input("Введите название файла \n")
        os.rename(fileName,fileNameTwo)

def createDir():
    dirName = input("Введите название каталога \n")
    os.mkdir(dirName)
    oldfile =  checkfile()
    fileInNewDir = dirName + "\\" + oldfile
    shutil.copyfile(oldfile,fileInNewDir)
    

def createTwoFile():
    oldFile = checkfile()
    shutil.copyfile(oldFile,oldFile+ "1")
    shutil.copyfile(oldFile,oldFile+ "2")
    os.remove(oldFile)

def createFileWithData():
    import datetime
    fileOutput = open("timeTxt.txt","w")
    fileOutput.write(str(datetime.datetime.today()) + "\n" )
    fileOutput.close()
    

while 1:
    print("Выбирете действие :")
    print("1 - определить, существует ли файл с заданным именем")
    print("2 - проверить, является ли проверяемый объект каталогом")
    print("3 - переименовать заданный файл")
    print("4 - создать в текущей папке подкаталог и скопировать туда заданный файл" )
    print("5 - сделать две копии файла с разными именами, исходный файл удалить")
    print("6 - записать во внешний текстовый файл текущую дату и время")

    choice = int(input("Ввдете цифру\n"))

    os.system("cls")

    if(choice == 1):
        checkfile()
    if(choice == 2):
        checkDir() 
    if(choice == 3):
        renameFile()
    if(choice == 4):
        createDir()
    if(choice == 5):
        createTwoFile()
    if(choice == 6):
        createFileWithData()

