class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular # Atributo
        self.saldo = saldo     # Atributo

    def depositar(self, monto):  # Método
        self.saldo += monto
        print(f"Has depositado {monto}. Saldo actual: {self.saldo}")

    def retirar(self, monto):    # Método
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Has retirado {monto}. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes.")

# Creación del objeto
cuenta1 = CuentaBancaria("Ana", 1000)

# Ejecución de métodos
cuenta1.depositar(500)
cuenta1.retirar(300)
cuenta1.retirar(1500)