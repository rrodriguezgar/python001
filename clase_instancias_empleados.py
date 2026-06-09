"""Ejercicio 17 - CLASE EMPLEADOS

Crear una clase "Empleados" en un fichero denominado clase_empleados.py.
Crear una clase que herede de empleados denominada "Aptitudes" con: lenguajes(programación), so(sistemas operativos que domina), e idioma.
Crear un nuevo fichero denominado clase_instancias_empleados.py con dos instancias de empleados utilizando esas clases.
"""

import clase_empleados

empleado1 = clase_empleados.Aptitudes("Juan", "Pérez", 30, "Python","windows","Alemán")
empleado2 = clase_empleados.Aptitudes("María", "Gómez", 25, "JavaScript", "windows","Inglés")

print(empleado1.apellido)
print(empleado2.idioma)