import math
from enum import Enum

class TrianguloTipo(Enum):
    EQUILATERO = "Equilátero"
    ISOSCELES  = "Isósceles"
    ESCALENO   = "Escaleno"


class Circulo:
    """Círculo definido por su radio en cm."""
    def __init__(self, radio: float):
        self.radio = radio

    def area(self) -> float:
        return math.pi * self.radio ** 2

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)


class Cuadrado:
    def __init__(self, lado: float):
        self.lado = lado

    def area(self) -> float:
        return self.lado ** 2

    def perimetro(self) -> float:
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return (self.base * self.altura) / 2

    def perimetro(self) -> float:
        return self.base + self.altura + self.hipotenusa()

    def hipotenusa(self) -> float:
        return math.hypot(self.base, self.altura)

    def tipo(self) -> TrianguloTipo:
        a = self.base
        b = self.altura
        c = self.hipotenusa()
        # comparaciones con tolerancia
        tol = 1e-9
        ab = abs(a - b) < tol
        ac = abs(a - c) < tol
        bc = abs(b - c) < tol
        if ab and ac and bc:
            return TrianguloTipo.EQUILATERO
        elif ab or ac or bc:
            return TrianguloTipo.ISOSCELES
        else:
            return TrianguloTipo.ESCALENO


def main():
    c = Circulo(radio=2)
    r = Rectangulo(base=1, altura=2)
    q = Cuadrado(lado=3)
    t = TrianguloRectangulo(base=3, altura=5)

    print("CÍRCULO")
    print(f"Radio      : {c.radio} cm")
    print(f"Área       : {c.area():.3f} cm²")
    print(f"Perímetro  : {c.perimetro():.3f} cm")
    print()

    print("RECTÁNGULO")
    print(f"Base       : {r.base} cm")
    print(f"Altura     : {r.altura} cm")
    print(f"Área       : {r.area():} cm^2")
    print(f"Perímetro  : {r.perimetro():} cm")
    print()

    print("CUADRADO")
    print(f"Lado       : {q.lado} cm")
    print(f"Área       : {q.area():} cm^2")
    print(f"Perímetro  : {q.perimetro():} cm")
    print()

    print("TRIÁNGULO RECTÁNGULO")
    print(f"Base       : {t.base} cm")
    print(f"Altura     : {t.altura} cm")
    print(f"Hipotenusa : {t.hipotenusa():.3f} cm")
    print(f"Área       : {t.area():} cm^2")
    print(f"Perímetro  : {t.perimetro():.3f} cm")
    print(f"Tipo       : {t.tipo().value}")
    print()


if __name__ == "__main__":
    main()
