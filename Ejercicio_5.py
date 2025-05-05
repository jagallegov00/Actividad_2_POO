from enum import Enum

class TipoCuenta(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"

class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria.
    """

    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0  # Saldo inicial

    def imprimir(self):
        print(f"Nombres del titular     : {self.nombres_titular}")
        print(f"Apellidos del titular   : {self.apellidos_titular}")
        print(f"Número de cuenta        : {self.numero_cuenta}")
        print(f"Tipo de cuenta          : {self.tipo_cuenta.value}")
        print(f"Saldo                   : ${self.saldo:,.2f}")

    def consultar_saldo(self):
        print(f"El saldo actual es      : ${self.saldo:,.2f}")

    def consignar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Se ha consignado ${valor:,.2f}. Nuevo saldo: ${self.saldo:,.2f}")
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Se ha retirado ${valor:,.2f}. Nuevo saldo: ${self.saldo:,.2f}")
            return True
        else:
            print("El valor a retirar debe ser menor o igual al saldo actual y mayor que cero.")
            return False

def main():
    cuenta = CuentaBancaria("Pedro", "Pérez", 123456789, TipoCuenta.AHORROS)
    cuenta.imprimir()
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)

if __name__ == "__main__":
    main()
