import os
from pathlib import Path

#fichero = open("2000-0.txt", "r")

#for linea in fichero:
#    print(linea)

#fichero.close()


with open("2000-0.txt", "r") as fichero:
    lineas=fichero.readlines(500) #lee 500 caracteres, no líneas
    for linea in lineas:
        print(linea.strip())



entrada= """ primera parte del ingenios hidalgo don Quijote de la Manchas

"""
#Crear un nuevo fichero y escribir en él
#with open("miquijote.txt", "x") as fichero:
#    fichero.write(entrada)



fichero_path=Path(Path.home(), "directorio_ficheros")
if not fichero_path.exists():
    fichero_path.mkdir()
   # os.makedirs(fichero_path)

fichero_path= fichero_path.joinpath("miquijote.txt")


entrada= """ En un lugar de la Mancha, de cuyo nombre no quiero
acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en
astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de
algo más vaca que carnero,
"""

#Añadir texto a un fichero existente
with open(fichero_path, "a") as fichero:
    fichero.write(entrada)


fichero_ruta=Path("dir1", "hola.py")
with fichero_ruta.open("r") as fichero:
    print(fichero.read())
  
