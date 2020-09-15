#!/usr/bin/python
"""
Creacion de programa para tomar notas y que los ordena en categorias 

categorias las cuales seran tomadas de las mismas notas creadas

basicamente el path vendra a ser 

/Documents/Anotaciones/categoria/nombre.txt

"""
import os, sys

PATH = "/Users/sebas/Documents/"

#verificacion de creacion de la carpeta para las anotaciones generales

for f in os.listdir(PATH):
    coincidencia = 0
    if f == "Anotaciones":
            coincidencia += 1
if coincidencia == 0:
    PATH = os.path.join(PATH, "Anotaciones") 
else:
    PATH = os.path.join(PATH, "Anotaciones") 
    os.mkdir(PATH)


#evaluar si la categoria existe o no para la creacion
def evaluarCategoria(category):
    for categorie in os.listdir(PATH):
        if categorie == category:
            return True
    return False

#creacion de la categoria para las anotaciones
def crearCategoria(category):
    newpath = os.path.join(PATH, category)
    os.mkdir(newpath)

#creacion de las anotaciones en su correspondiente categoria 
def crearAnotacion(name,category,anotacion):
    newpath = os.path.join(PATH, category)
    newpath = newpath + "/"
    for f in os.listdir(newpath):

        if f == name+".txt":
            name = name + "0"
            file = open(newpath+name+".txt","wt")
            file.write(anotacion)
        else:
            file = open(newpath+name+".txt","wt")
            file.write(anotacion)

def main(name,category,anotacion):
    if (evaluarCategoria(category) == True):
        crearAnotacion(nombre, category, note)
    else:
        crearCategoria(category)
        crearAnotacion(nombre, category, note)


nombre = input("Ingrese nombre de anotacion ")
category = input("Ingrese la categoria")
note = input("Ingrese anotacion")

main(nombre, category, note)
