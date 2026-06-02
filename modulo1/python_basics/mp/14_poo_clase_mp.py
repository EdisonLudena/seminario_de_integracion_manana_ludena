class Jugador:
    deporte = "Fútbol"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad   = edad

    def saludar(self):
        return f"Hola, soy el jugador {self.nombre} y tengo {self.edad} años."

    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad}.")

    def __str__(self):
        return f"Jugador({self.nombre}, {self.edad})"

    def __repr__(self):
        return f"Jugador(nombre={self.nombre!r}, edad={self.edad!r})"

ana  = Jugador("Ana García", 28)
luis = Jugador("Luis Pérez", 31)

print(ana.saludar())
print(luis.saludar())
ana.cumplir_anios()
print(str(ana))
print(repr(ana))
print(Jugador.deporte)