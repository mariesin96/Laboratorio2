class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca   # Atributo
        self.modelo = modelo # Atributo
        self.color = color   # Atributo

    def arrancar(self):      # Método
        print(f"El coche {self.marca} {self.modelo} de color {self.color} ha arrancado.")

# Creación del objeto
coche1 = Coche("Ford", "Mustang", "rojo")

# Ejecución de método
coche1.arrancar()