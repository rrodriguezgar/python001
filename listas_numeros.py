numeros=[0,1,2,3,4,5,6,7,8,9,10]

print(numeros)

for num in numeros:
    print(num)


print("Min", min(numeros))
print("Max", max(numeros))

segunda_lista=[numeros[0], numeros[-1]]

for num in segunda_lista:
    print(num)


tercera_lista=[min(numeros), max(numeros)]

for num in tercera_lista:
    print(num)