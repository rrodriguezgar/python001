lista1= [1, 2, 3, 4, 7,5]
lista2 = [lista1[0], lista1[-1]]
lista3 = [min(lista1), max(lista1)]

print(lista1)
print(lista2)
print(lista3)

for i in range(10):
    if i % 2 != 0:     
        print(f"{i} es un número impar")

print("bucle while")
contador = 0
while contador <= 10:
    if contador % 2 != 0:
        print(f"{contador} es un número impar")
    contador += 1
    

print("Fin" )