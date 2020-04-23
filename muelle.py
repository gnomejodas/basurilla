#!/usr/bin/python3

import csv
import sys
import os
import re

ficheros =[] # los ficheros que has arrastrado
todos = os.listdir("./") # Todos los archivos del directorio
regex = re.compile(r'.+(?:png|jpg|jpeg|gif)+$')
imagenes = list(filter(regex.match, todos)) #Esta es una lista de los ficheros que acaban en png, jpg, jpeg o gif

#imagenes = [os.path.splitext(i)[0] for i in imagenes] #nombres de las imagenes sin extensión

#print(imagenes)

#Vamos a cargar los ficheros que se introducen como argumentos, por si metes más de 1 csv
for arg in sys.argv:
    ficheros.append(arg)
ficheros.pop(0)


#print(ficheros)



for listadecsv in ficheros:
#    print (listadecsv)
    with open(listadecsv) as fichero_csv:
        lector_csv = csv.reader(fichero_csv, delimiter = ',') #el delimitador es "," y permite crear una lista de listas que contienen 2 valores
        #cada lista contiene los valores del csv
        for fila in lector_csv: #fila es la lista con los 2 nombres de imagen, el de partida y el final
            
            #fila[0] es lo que queremos reemplazar, y fila[1] es por lo que lo queremos reemplazar
            if not fila: continue
            for nombre_imagen in imagenes:
                patron_viejo = os.path.splitext(fila[0])[0]
                patron_nuevo = os.path.splitext(fila[1])[0]
                nuevo_nombre = nombre_imagen.replace(patron_viejo,patron_nuevo)
                if (nombre_imagen != nuevo_nombre):
                    os.rename(nombre_imagen,nuevo_nombre)
                    print(nombre_imagen, "se renombŕo a", nuevo_nombre)








