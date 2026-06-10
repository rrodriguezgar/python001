import pandas as pd

fichero_csv = "catalogo_cf.csv"
fichero_tsv = "catalogo_cf.tsv"

escribir_csv = "catalogo_csv.csv"
escribir_tsv = "catalogo_tsv.tsv"

leer_csv = pd.read_csv(fichero_csv, encoding="ISO-8859-1")
leer_tsv = pd.read_csv(fichero_tsv, sep="\t", encoding="UTF-8-SIG")

#Imprimir las primeras 20 filas de cada DataFrame
#print(leer_csv.head(20))
#print(leer_tsv.head(20))

with open(escribir_csv, "w", encoding="UTF-8",newline="") as write_csv:
          write_csv.write(leer_csv.head(20).to_csv(sep=",", index=False))

with open(escribir_tsv, "w", encoding="UTF-8-SIG") as write_tsv:
          write_tsv.write(leer_tsv.head(20).to_csv( encoding="UTF-8-SIG",sep="\t",index=False))
