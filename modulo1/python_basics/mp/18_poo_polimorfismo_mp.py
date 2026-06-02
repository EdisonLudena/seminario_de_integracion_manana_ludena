class MetricaScouting:
    def __init__(self, reporte_id, valoracion):
        self.reporte_id = reporte_id
        self.valoracion = valoracion

    def registrar(self):
        raise NotImplementedError("Las subclases deben implementar registrar()")

    def __str__(self):
        return f"{self.__class__.__name__} → Reporte {self.reporte_id}"

class MetricasTecnicas(MetricaScouting):
    def __init__(self, reporte_id, valoracion, control=80):
        super().__init__(reporte_id, valoracion)
        self.control = control

    def registrar(self):
        return f"⚽ Técnicas en Reporte {self.reporte_id}: [Control: {self.control}] {self.valoracion}"

class MetricasTacticas(MetricaScouting):
    MAX_CHARS = 160

    def registrar(self):
        msg = self.valoracion[:self.MAX_CHARS]
        return f"🧠 Tácticas en Reporte {self.reporte_id}: {msg}"

class HistorialAntropometrico(MetricaScouting):
    def registrar(self):
        return f"📏 Biometría en Reporte {self.reporte_id}: {self.valoracion[:50]}..."

class TestsRendimiento(MetricaScouting):
    def __init__(self, reporte_id, valoracion):
        super().__init__(reporte_id, valoracion)

    def registrar(self):
        return f"🏃 Físico en Reporte {self.reporte_id}: {self.valoracion}"


def consolidar_dashboard(metricas: list):
    for metrica in metricas:
        print(f"  {metrica.registrar()}")

alertas = [
    MetricasTecnicas("ana@email.com", "Tu pedido fue enviado", "Pedido #1234"),
    MetricasTacticas("600111222", "Tu pedido está en camino"),
    HistorialAntropometrico("dispositivo-abc", "¡Nuevo mensaje recibido!"),
    TestsRendimiento("alertas", "Servidor caído — revisar urgente"),
]

print("Enviando notificaciones:")
consolidar_dashboard(alertas)


class EventosLive:
    def leer(self):   return "datos desde disco local"
    def escribir(self, datos): print(f"Guardando en disco: {datos[:30]}...")

class LesionesRegistro:
    def leer(self):   return "datos desde la nube"
    def escribir(self, datos): print(f"Subiendo a la nube: {datos[:30]}...")

class ValoracionEconomica:
    def leer(self):   return "datos desde base de datos"
    def escribir(self, datos): print(f"Insertando en BD: {datos[:30]}...")


def procesar_archivo(archivo):
    contenido = archivo.leer()
    print(f"Procesando: {contenido}")
    archivo.escribir(f"resultado_{contenido}")

for archivo in [EventosLive(), LesionesRegistro(), ValoracionEconomica()]:
    procesar_archivo(archivo)