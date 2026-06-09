# Ejemplo de uso de la biblioteca re
import re
# Encontrar coincidencias
texto = "Hoy es un día magnífico y maravilloso"
exp_reg = re.search("^Hoy.*oso$", texto)
print(exp_reg)

#Encuentra todas las coincidencias
exp_reg2 = re.findall("ma", texto)
print(exp_reg2)

 # Reemplazar espacio vacío
exp_reg3 = re.sub("\\s", " ", texto)
print(exp_reg3)

# Para buscar mayúsculas o minúsculas indistintamente se puede utilizar el método lower():
 # Obtener todo el texto
exp_reg4 = re.match(r'.*', texto.lower())
print(exp_reg4.group(0))

print("Glob")
import glob
for fichero in glob.glob('*'):
    print(fichero)

print("iGlob")
ficheros_py = glob.iglob("*.py")
print("Lista de ficheros .py: ")
for ficheros in ficheros_py:
    print(ficheros)

print("fnmatch y os ")
import fnmatch
import os

texto = "ejemplo*.py"
ficheros=os.listdir('.')

print(fnmatch.filter(ficheros, texto))

for fichero in ficheros:
    if fnmatch.fnmatch(fichero, texto):
        print(fichero)