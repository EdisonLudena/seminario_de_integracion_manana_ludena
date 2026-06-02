vacio = {}
jugador = {"nombre": "Ana", "edad": 28, "ciudad": "Madrid"}
config_app = dict(host="localhost", puerto=5432, debug=True)

print(jugador["nombre"])
print(jugador.get("email"))
print(jugador.get("email", "N/A"))

jugador["email"] = "ana@email.com"
jugador["edad"] = 29
del jugador["ciudad"]
valor_eliminado = jugador.pop("email")
print(jugador)

print("nombre" in jugador)
print("ciudad" in jugador)

print(jugador.keys())
print(jugador.values())
print(jugador.items())

for clave, valor in jugador.items():
    print(f"  {clave}: {valor}")

jugador.update({"ciudad": "Barcelona", "tel": "600111222"})
print(jugador)

extra = {"cargo": "Desarrolladora", "activo": True}
completo = jugador | extra
print(completo)

entidad = {
    "nombre": "TechCorp",
    "empleados": {
        1: {"nombre": "Ana", "depto": "tech"},
        2: {"nombre": "Luis", "depto": "ventas"},
    },
    "sedes": ["Madrid", "Barcelona"]
}

print(entidad["empleados"][1]["nombre"])
entidad["empleados"][3] = {"nombre": "Marta", "depto": "rrhh"}

jugador.setdefault("pais", "España")
jugador.setdefault("nombre", "Otro")