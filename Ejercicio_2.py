from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"

class Planeta:
    """
    Clase que modela un planeta del sistema solar.

    Atributos:
    - nombre (str): Nombre del planeta.
    - cantidad_satelites (int): Número de satélites naturales.
    - masa (float): Masa en kilogramos.
    - volumen (float): Volumen en kilómetros cúbicos.
    - diametro (int): Diámetro en kilómetros.
    - distancia_sol (int): Distancia media al Sol en kilómetros.
    - tipo (TipoPlaneta): Tipo de planeta según su tamaño.
    - es_observable (bool): Si es observable a simple vista.
    """

    # Unidad astronómica en kilómetros
    UA_KM = 149597870

    def __init__(self,
                 nombre: str = None,
                 cantidad_satelites: int = 0,
                 masa: float = 0.0,
                 volumen: float = 0.0,
                 diametro: int = 0,
                 distancia_sol: int = 0,
                 tipo: TipoPlaneta = None,
                 es_observable: bool = False):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable

    def imprimir_datos(self):
        print(f"Nombre del planeta       : {self.nombre}")
        print(f"Cantidad de satélites    : {self.cantidad_satelites}")
        print(f"Masa (kg)                : {self.masa:.3e}")
        print(f"Volumen (km^3)           : {self.volumen:.3e}")
        print(f"Diámetro (km)            : {self.diametro}")
        print(f"Distancia al Sol (km)    : {self.distancia_sol}")
        print(f"Tipo de planeta          : {self.tipo.name if self.tipo else 'N/D'}")
        print(f"Observable a simple vista: {self.es_observable}")

    def calcular_densidad(self) -> float:
        """
        Calcula la densidad como masa / volumen.
        Retorna 0 si el volumen es cero para evitar división por cero.
        """
        return self.masa / self.volumen if self.volumen > 0 else 0.0

    def es_planeta_exterior(self) -> bool:
        """
        Determina si el planeta está más allá del cinturón de asteroides.
        El cinturón está entre 2.1 UA y 3.4 UA.
        """
        limite_exterior_km = 3.4 * Planeta.UA_KM
        return self.distancia_sol > limite_exterior_km


def main():
    tierra = Planeta(
        nombre="Tierra",
        cantidad_satelites=1,
        masa=5.9736e24,
        volumen=1.08321e12,
        diametro=12742,
        distancia_sol=150000000,  # en km
        tipo=TipoPlaneta.TERRESTRE,
        es_observable=True
    )

    jupiter = Planeta(
        nombre="Júpiter",
        cantidad_satelites=1,
        masa=1.899e27,
        volumen=1.4313e15,
        diametro=139820,
        distancia_sol=750000000,  # en km
        tipo=TipoPlaneta.GASEOSO,
        es_observable=True
    )

    for planeta in (tierra, jupiter):
        planeta.imprimir_datos()
        print(f"Densidad del planeta     : {planeta.calcular_densidad():.15e}")
        print(f"Es plantea exterior      : {planeta.es_planeta_exterior()}")
        print()

if __name__ == "__main__":
    main()
