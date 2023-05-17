# Crear dos objetos de la clase 01
# objeto 01
# crear
# Presentar objeto; usar el método __st__
# objeto 02
# crear ingresando valores por teclado
# Presentar objeto; usar el método __st__

from mis_clases import CalcularPromedio

print("\nIngrese datos para el primer estudiante")
nombre = input("Ingrese sus nombres: ")
apellido = input("Ingrese sus apellidos: ")
nota1 = float(input("Ingrese nota 1: "))
nota2 = float(input("Ingrese nota 2: "))
nota3 = float(input("Ingrese nota 3: "))

estudiante1 = CalcularPromedio(nombre, apellido, nota1, nota2, nota3)  # Primer objeto
estudiante1.calcular()

print("\nIngrese datos para el segundo estudiante")
nom = input("Ingrese sus nombres: ")
apel = input("Ingrese sus apellidos: ")
nota1 = float(input("Ingrese nota 1: "))
nota2 = float(input("Ingrese nota 2: "))
nota3 = float(input("Ingrese nota 3: "))

estudiante2 = CalcularPromedio(nom, apel, nota1, nota2, nota3)  # Segundo objeto
estudiante2.calcular()
print("----------------------------------------------")
print(estudiante1)
print("----------------------------------------------")
print(estudiante2)



