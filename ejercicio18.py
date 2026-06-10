import pandas as pd
import shutil
import os
from pathlib import Path

#wget.download('https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/36680.csv')

poblacion_csv="36680.csv"
poblacion_tsv="36680.tsv"

poblacion_csv_copia="36680_copia.csv"

leer_csv = pd.read_csv(poblacion_csv,sep=";", encoding="UTF-8")

#1.- Crear una copia y luego convertir el fichero .csv a .tsv
shutil.copy(src=poblacion_csv, dst=poblacion_csv_copia)

#with open(poblacion_csv_copia, "w", encoding="UTF-8",newline="") as write_csv:
#          write_csv.write(leer_csv.to_csv(sep=";", index=False))

with open(poblacion_tsv, "w", encoding="UTF-8",newline="") as write_tsv:
          write_tsv.write(leer_csv.to_csv(encoding="UTF-8",sep="\t", index=False))

#2.- Crear un directorio y mover la copia del fichero .csv dentro
ruta_app = Path(__file__).resolve().parent
fichero_path=Path(ruta_app, "poblacion")
if not fichero_path.exists():
    fichero_path.mkdir()
   # os.makedirs(fichero_path)

shutil.move(src=poblacion_csv_copia, dst=fichero_path.joinpath(poblacion_csv_copia))

#3.- Escribir en un nuevo fichero las primeras 100 líneas del fichero .tsv

#4.- Convertir el fichero con formato .csv a .xlsx
leer_fichero_toexcel = pd.read_csv(r"36680.csv",sep=";", encoding="UTF-8")
escribir_excel = "36680.xlsx"

leer_fichero_toexcel.to_excel(r"36680.xlsx", index=False, header=True)
