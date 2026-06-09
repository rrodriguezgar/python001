"""Ejercicio 17 - CLASE EMPLEADOS

Crear una clase "Empleados" en un fichero denominado clase_empleados.py.
Crear una clase que herede de empleados denominada "Aptitudes" con: lenguajes(programación), so(sistemas operativos que domina), e idioma.
Crear un nuevo fichero denominado clase_instancias_empleados.py con dos instancias de empleados utilizando esas clases.
"""

class Empleados:
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario


class Aptitudes(Empleados):
    def __init__(self, nombre, apellido, salario, lenguajes, so, idioma):
        super().__init__(nombre, apellido, salario)
        self.lenguajes = lenguajes
        self.so = so
        self.idioma = idioma


