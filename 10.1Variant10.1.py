# Тема "БД" - количество определенной марки автомобиля на складе

import os

dictCountCars = {}
fileSave = open("filesOutput/fileOutput10.1.txt", "w", encoding='utf-8')


def firstWrite():
    c_Count = int(input("Вветие количество автомобилей \n"))
    c_Name = input("Введите название автомобиля \n")
    dictCountCars.update({c_Name: c_Count})

def checkfile(str = "", FileName = ""):
    if(str == ""):
        FileName = input("Введите путь к файлу и  название файла \n")
    if(os.path.exists(FileName) or os.path.exists(str)):
        print("Файл существует")
        return FileName
    else:
        print("Файл не существует ")
        return False

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
        fileSave.write(str(dictCountCars))
    if (choice == 3):
        pass
    if (choice == 4):
        pass
    if (choice == 5):
        pass
    if (choice == 6):
        pass
    if (choice == 7):
        pass
    if (choice == 8):
        break

    print(dictCountCars)

fileSave.close()