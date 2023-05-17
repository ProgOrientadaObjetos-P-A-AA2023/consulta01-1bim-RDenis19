# Crear dos objetos de la clase 02
# objeto 01
# crear
# Presentar objeto; usar el método __st__
# objeto 02
# crear ingresando valores por teclado
# Presentar objeto; usar el método __st__

from mis_clases import Profesor

print("\nIngrese los datos del primer profesor")
nombre = input("Ingrese sus nombres: ")
apellido = input("Ingrese sus apellidos: ")
cedula = input("Ingrese su cedula: ")
sueldo = float(input("Ingrese su sueldo: "))

profesor1 = Profesor(nombre, apellido, cedula, sueldo)  # Primer objeto
profesor1.calcular()

print("\nIngrese los dato del segundo profesor")
nombre = input("Ingrese sus nombres: ")
apellido = input("Ingrese sus apellidos: ")
cedula = input("Ingrese su cedula: ")
sueldo = float(input("Ingrese su sueldo: "))

profesor2 = Profesor(nombre, apellido, cedula, sueldo)  # Segundo objeto
profesor2.calcular()
print("----------------------------------------------")
print(profesor1)
print("----------------------------------------------")
print(profesor2)




