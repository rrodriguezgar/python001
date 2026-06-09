#num1 =  int(input("Ingresa un número: "))
#num2 =  int(input("Ingresa otro número: "))

#if num1== num2:
#    print("Los números son iguales")
#elif num1 > num2:
#   print(f"El número mayor es: {num1}")
#else:
#     print(f"El número mayor es:7 {num2}")

#ejercicio 5
from datetime import datetime

nombre = str(input("Ingresa tu nombre: "))
edad = int(input("Ingresa tu edad: "))

ahora = datetime.now()
anio_actual = ahora.year    

print(f"Hola {nombre}. Tendrás 100 años en el año {anio_actual + (100 - edad)}")    


#ejercicio 6
num = int(input("Ingresa un número: "))

print(f"El número {num} es par" if num % 2 == 0 else f"El número {num} es impar")

print(f"El número {num} es múltiplo de 4" if num % 4 == 0 else f"El número {num} no es múltiplo de 4") if num > 0 else f"El número {num} es cero"

