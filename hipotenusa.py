import math

cateto1 = 4
cateto2 = 3

hipotenusa = math.sqrt((cateto1**2 +cateto2**2))


hipotenusa2 = math.hypot(3,4)
print(hipotenusa)
print(hipotenusa2)

print("La hipotenusa es igual a la suma del cuadrado de los catetos")
print("Cateto 1 =", cateto1)
print("Cateto 2 =", cateto2)
print("Hipotenusa =", hipotenusa)

print(f"La hipotenusa de los catetos {cateto1} y {cateto2} es {hipotenusa}")

print(id(cateto1))
print(type(cateto1))