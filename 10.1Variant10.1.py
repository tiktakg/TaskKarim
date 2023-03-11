# Тема "БД" - количество определенной марки автомобиля на складе

import os

dictCountCars = {}



def firstWrite():
    c_Count = int(input("Вветие количество автомобилей \n"))
    c_Name = input("Введите название автомобиля \n")
    dictCountCars.update({c_Name:c_Count})


def checkfile(str="", FileName=""):
    if (str == ""):
        FileName = input("Введите путь к файлу и  название файла \n")
    if (os.path.exists(FileName) or os.path.exists(str)):
        print("Файл существует")
        return FileName
    else:
        print("Файл не существует ")
        return False

def writeDataInFile():
    with open("filesOutput/fileOutput10.1.txt", "w") as f:
        for key, value in dictCountCars.items():
            f.write(f"{key}: {value}\n")

def readByFile():
    with open("filesOutput/fileOutput10.1.txt", "r") as file:
         for line in file:
            key, value = line.strip().split(":")
            dictCountCars[key] = value

def updateAndDelteData():
    dictCountCars[input("Введите название марки, чье кол-во автомобилей хотите изменить \n")] = int(input("Введите количество автомобилей на  которые хотите изменить \n"))
    del dictCountCars[input("Введите название марки, которую хотите удалить \n")]

def serchDataByKey():
   print(dictCountCars[input("Введите название марки, чье кол-во автомобилей хотите посмотреть \n")])

def sortDataByKey():
   sorted_dict = dict(sorted(dictCountCars.items(), key=lambda x: x[0]))
   

while 1:
    print("Выбирете действие :")
    print("1 - первичного заполнения словаря с клавиатуры")
    print("2 - сохранения данных во внешний файл")
    print("3 - считывания данных в словарь при наличии связанного внешнего файла")
    print("4 - добавления данных в словарь с последующим сохранением в файле данных")
    print("5 - изменения и удаления информации")
    print("6 - поиска информации по ключу")
    print("7 - сортировки информации по ключу")
    print("8 - Выйти из программы")

    choice = int(input("Ввдете цифру\n"))

    if (choice == 1):
        firstWrite()
    if (choice == 2):
        writeDataInFile()
    if (choice == 3):
        readByFile()
    if (choice == 4):
        firstWrite()
        writeDataInFile()
    if (choice == 5):
        updateAndDelteData()
    if (choice == 6):
        serchDataByKey()
    if (choice == 7):
        sortDataByKey()
    if (choice == 8):
        break
