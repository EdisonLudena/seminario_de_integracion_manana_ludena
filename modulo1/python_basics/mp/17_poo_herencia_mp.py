class Persona:
    def __init__(self, nombre, ciudad, fecha_registro):
        self.nombre = nombre
        self.ciudad = ciudad
        self.fecha_registro = fecha_registro
        self._rendimiento_base = 0

    def entrenar(self, incremento):
        self._rendimiento_base += incremento
        return self

    def descansar(self, decremento):
        self._rendimiento_base = max(0, self._rendimiento_base - decremento)
        return self

    def __str__(self):
        return f"{self.nombre} {self.ciudad} ({self.fecha_registro}) — {self._rendimiento_base} pts"

class Entrenador(Persona):
    def __init__(self, nombre, ciudad, fecha_registro, categorias_cargo=4):
        super().__init__(nombre, ciudad, fecha_registro)
        self.categorias_cargo = categorias_cargo

    def dar_instrucciones(self):
        return f"{self.nombre} {self.ciudad}: ¡Presionen arriba!"

    def __str__(self):
        return f"{super().__str__()} ({self.categorias_cargo} categorías a cargo)"

class Scout(Persona):
    def __init__(self, nombre, ciudad, fecha_registro, reportes_hechos):
        super().__init__(nombre, ciudad, fecha_registro)
        self.reportes_hechos = reportes_hechos

    def buscar_talento(self):
        return f"⚽ {self.nombre} está evaluando prospectos de élite!"

    def __str__(self):
        return f"{super().__str__()} ({self.reportes_hechos} reportes generados)"

class JugadorElite(Entrenador):
    def __init__(self, nombre, ciudad, fecha_registro, valor_mercado):
        super().__init__(nombre, ciudad, fecha_registro)
        self.__valor_mercado = valor_mercado
        self.__estado_fisico = 100

    def rehabilitar(self, porcentaje=100):
        self.__estado_fisico = min(100, self.__estado_fisico + porcentaje)
        return self

    @property
    def valor_actualizado(self):
        return self.__valor_mercado * self.__estado_fisico / 100

    def __str__(self):
        return (f"{super().__str__()} | "
                f"Salud Física: {self.__estado_fisico}% | "
                f"Valor Estimado: {self.valor_actualizado:.0f}K USD")

prospecto = JugadorElite("Edison Ludeña", "Quito", 2026, 500)
prospecto.entrenar(100)
print(prospecto)

print(isinstance(prospecto, JugadorElite))
print(isinstance(prospecto, Entrenador))
print(isinstance(prospecto, Persona))
print(isinstance(prospecto, Scout))

print(JugadorElite.__mro__)