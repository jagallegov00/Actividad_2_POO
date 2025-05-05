from enum import Enum

class TipoCombustible(Enum):
    GASOLINA    = "Gasolina"
    BIOETANOL   = "Bioetanol"
    DIESEL      = "Diésel"
    BIODIESEL   = "Biodiésel"
    GAS_NATURAL = "Gas natural"


class TipoAutomovil(Enum):
    CIUDAD      = "Carro de ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO    = "Compacto"
    FAMILIAR    = "Familiar"
    EJECUTIVO   = "Ejecutivo"
    SUV         = "SUV"


class Color(Enum):
    BLANCO   = "Blanco"
    NEGRO    = "Negro"
    ROJO     = "Rojo"
    NARANJA  = "Naranja"
    AMARILLO = "Amarillo"
    VERDE    = "Verde"
    AZUL     = "Azul"
    VIOLETA  = "Violeta"


class Automovil:
    def __init__(self,
                 marca: str,
                 modelo: int,
                 motor: float,
                 tipo_combustible: TipoCombustible,
                 tipo_automovil: TipoAutomovil,
                 numero_puertas: int,
                 cantidad_asientos: int,
                 velocidad_maxima: int,
                 color: Color):
        # Atributos
        self._marca = marca
        self._modelo = modelo
        self._motor = motor
        self._tipo_combustible = tipo_combustible
        self._tipo_automovil = tipo_automovil
        self._numero_puertas = numero_puertas
        self._cantidad_asientos = cantidad_asientos
        self._velocidad_maxima = velocidad_maxima
        self._color = color
        self._velocidad_actual = 0

    # --- Métodos get ---
    def get_marca(self) -> str:
        return self._marca

    def get_modelo(self) -> int:
        return self._modelo

    def get_motor(self) -> float:
        return self._motor

    def get_tipo_combustible(self) -> TipoCombustible:
        return self._tipo_combustible

    def get_tipo_automovil(self) -> TipoAutomovil:
        return self._tipo_automovil

    def get_numero_puertas(self) -> int:
        return self._numero_puertas

    def get_cantidad_asientos(self) -> int:
        return self._cantidad_asientos

    def get_velocidad_maxima(self) -> int:
        return self._velocidad_maxima

    def get_color(self) -> Color:
        return self._color

    def get_velocidad_actual(self) -> int:
        return self._velocidad_actual

    # --- Métodos set ---
    def set_marca(self, marca: str):
        self._marca = marca

    def set_modelo(self, modelo: int):
        self._modelo = modelo

    def set_motor(self, motor: float):
        self._motor = motor

    def set_tipo_combustible(self, tipo: TipoCombustible):
        self._tipo_combustible = tipo

    def set_tipo_automovil(self, tipo: TipoAutomovil):
        self._tipo_automovil = tipo

    def set_numero_puertas(self, puertas: int):
        self._numero_puertas = puertas

    def set_cantidad_asientos(self, asientos: int):
        self._cantidad_asientos = asientos

    def set_velocidad_maxima(self, vmax: int):
        self._velocidad_maxima = vmax

    def set_color(self, color: Color):
        self._color = color

    def set_velocidad_actual(self, velocidad: int):
        if velocidad < 0:
            print("No se puede establecer una velocidad negativa.")
        elif velocidad > self._velocidad_maxima:
            print("No se puede establecer una velocidad mayor a la máxima.")
        else:
            self._velocidad_actual = velocidad

    # Control de velocidad
    def acelerar(self, incremento: int):
        nueva = self._velocidad_actual + incremento
        if nueva > self._velocidad_maxima:
            print(f"No se puede acelerar más allá de {self._velocidad_maxima} km/h.")
        else:
            self._velocidad_actual = nueva

    def desacelerar(self, decremento: int):
        nueva = self._velocidad_actual - decremento
        if nueva < 0:
            print("No se puede reducir la velocidad por debajo de 0 km/h.")
        else:
            self._velocidad_actual = nueva

    def frenar(self):
        self._velocidad_actual = 0

    #tiempo estimado
    def calcular_tiempo_llegada(self, distancia: float) -> float:
        if self._velocidad_actual <= 0:
            print("La velocidad actual debe ser mayor que cero para calcular tiempo de llegada.")
            return float('inf')
        return distancia / self._velocidad_actual

    def imprimir_datos(self):
        print(f"Marca               : {self._marca}")
        print(f"Modelo (año)        : {self._modelo}")
        print(f"Motor (L)           : {self._motor}")
        print(f"Tipo combustible    : {self._tipo_combustible.value}")
        print(f"Tipo automóvil      : {self._tipo_automovil.value}")
        print(f"Número de puertas   : {self._numero_puertas}")
        print(f"Asientos            : {self._cantidad_asientos}")
        print(f"Velocidad máxima    : {self._velocidad_maxima} km/h")
        print(f"Color               : {self._color.value}")
        print(f"Velocidad actual    : {self._velocidad_actual} km/h")
        print()

def main():
    auto1 = Automovil(
        marca="Ford",
        modelo=2018,
        motor=3.0,
        tipo_combustible=TipoCombustible.DIESEL,
        tipo_automovil=TipoAutomovil.EJECUTIVO,
        numero_puertas=5,
        cantidad_asientos=6,
        velocidad_maxima=250,
        color=Color.NEGRO
    )


    auto1.imprimir_datos()
    print("Establecer velocidad actual a 100 km/h")
    auto1.set_velocidad_actual(100)
    print(f"Velocidad actual: {auto1.get_velocidad_actual()} km/h\n")
    print("Acelerar +20 km/h")
    auto1.acelerar(20)
    print(f"Velocidad actual: {auto1.get_velocidad_actual()} km/h\n")
    print("Desacelerar 50 km/h")
    auto1.desacelerar(50)
    print(f"Velocidad actual: {auto1.get_velocidad_actual()} km/h\n")
    print("Frenar")
    auto1.frenar()
    print(f"Velocidad actual: {auto1.get_velocidad_actual()} km/h\n")
    # Intento de desacelerar por debajo de 0
    print("Intento de desacelerar 20 km/h")
    auto1.desacelerar(20)

if __name__ == "__main__":
    main()
