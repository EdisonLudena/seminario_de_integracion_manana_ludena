class ValoracionEconomica:
    def __init__(self, jugador_id, valor_estimado_inicial=0):
        self.jugador_id = jugador_id
        self.__valor_estimado = valor_estimado_inicial
        self.__historial = []
        self.__activa = True
        self.__registrar(f"Cuenta creada con {valor_estimado_inicial}€")

    @property
    def valor_estimado(self):
        return self.__valor_estimado

    @property
    def activa(self):
        return self.__activa

    @property
    def historial(self):
        return list(self.__historial)

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.__valor_estimado += cantidad
        self.__registrar(f"Depósito: +{cantidad}€")
        return self

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.__valor_estimado:
            raise ValueError(f"Saldo insuficiente (disponible: {self.__valor_estimado}€)")
        self.__valor_estimado -= cantidad
        self.__registrar(f"Retiro: -{cantidad}€")
        return self

    def transferir(self, destino, cantidad):
        self.retirar(cantidad)
        destino.depositar(cantidad)
        self.__registrar(f"Transferencia a {destino.jugador_id}: -{cantidad}€")
        return self

    def __registrar(self, operacion):
        from datetime import datetime
        hora = datetime.now().strftime("%H:%M:%S")
        self.__historial.append(f"[{hora}] {operacion}")

    def __str__(self):
        return f"Cuenta({self.jugador_id}: {self.__valor_estimado}€)"


c1 = ValoracionEconomica("Ana García", 1000)
c2 = ValoracionEconomica("Luis Pérez", 500)

c1.depositar(500).retirar(200)
c1.transferir(c2, 300)

print(c1)
print(c2)
print(f"Saldo Ana: {c1.valor_estimado}€")

for entrada in c1.historial:
    print(f"  {entrada}")