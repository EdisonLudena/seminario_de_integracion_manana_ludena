from abc import ABC, abstractmethod

class Contrato(ABC):
    def __init__(self, estado="Activo"):
        self.estado = estado

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

    def describir(self) -> str:
        return (f"{self.__class__.__name__} {self.estado}: "
                f"área={self.area():.2f}, perímetro={self.perimetro():.2f}")


class Circulo(Contrato):
    def __init__(self, radio, estado="Activo"):
        super().__init__(estado)
        self.radio = radio

    def area(self):
        import math
        return math.pi * self.radio ** 2

    def perimetro(self):
        import math
        return 2 * math.pi * self.radio

class Rectangulo(Contrato):
    def __init__(self, ancho, alto, estado="Activo"):
        super().__init__(estado)
        self.ancho = ancho
        self.alto  = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Triangulo(Contrato):
    def __init__(self, a, b, c, estado="Activo"):
        super().__init__(estado)
        self.a, self.b, self.c = a, b, c

    def perimetro(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimetro() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


formas = [Circulo(5, "Cancelado"), Rectangulo(4, 6, "Basico"), Triangulo(3, 4, 5, "Premium")]

for forma in formas:
    print(forma.describir())

area_total = sum(f.area() for f in formas)
print(f"Área total: {area_total:.2f}")