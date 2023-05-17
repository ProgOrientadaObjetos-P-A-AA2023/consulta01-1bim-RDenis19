"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class CalcularPromedio:
        def __init__(self, no, ap, a, b, c):
            self.nom = no
            self.apel = ap
            self.nota1 = a
            self.nota2 = b
            self.nota3 = c

        def calcular(self):
            self.promedioFinal = (self.nota1 + self.nota2 + self.nota3) / 3

        def __str__(self):
            return f"Nombre: {self.nom}\nApellido: {self.apel}\nNota 1: {self.nota1}\n" \
                   f"Nota 2: {self.nota2}\nNota 3: {self.nota3}\nPromedio Final: {self.promedioFinal}\n"
# clase 02
class Profesor:
    def __init__(self, nom, ape, ced, su):
        self.nombre = nom
        self.apellido = ape
        self.cedula = ced
        self.sueldo = su
        self.sueldoFinal = 0

    def calcular(self):
        self.sueldoFinal = (self.sueldo * 0.6) + self.sueldo

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nCedula: {self.cedula}\nSueldo: {self.sueldo}\nSueldo Total: {self.sueldoFinal}\n"





