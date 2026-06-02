print("Listas")
print("Crear listas")
vacia = []
print(vacia)
dorsales = [1, 2, 3, 4, 5, 6, 7]
print(dorsales)
jugadores = ["Juan", "Pedro", "Carlos", "Maria", "Petra", "Juana"]
print(jugadores)
mixta = [1, "Gol", "Rival", True, None, 3.4]
print(mixta)
aninada = [1, [5, 5, [6, 4, 4]], 5, 7]
print(aninada)
print("Acceder a elementos de la lista")
print(jugadores[0])
print(jugadores[-1])
print(jugadores[1:3])
print(jugadores[::-1])

print("CRUD en listas")
equipos = ["LDU", "Barcelona", "Emelec", "Independiente"]
equipos.append("Aucas")
print(equipos)
equipos.insert(1, "El Nacional")
print(equipos)
equipos.extend(["Macará", "Delfín"])
equipos[0] = "Deportivo Quito"
print(equipos)
equipos.remove("Emelec")
print(equipos)
eliminado = equipos.pop()
print(equipos)
eliminado = equipos.pop(0)
print(equipos)
del equipos[0]
print(equipos)

print("buscar valores en los elementos de una lista")
print("Macará" in equipos)
print(equipos.index("Macará"))
print(equipos.count("Macará"))

print("ordenar listas")
minutos_jugados = [5, 2, 9, 1, 5, 6, 34, 9, 0, 1, 2]
print(minutos_jugados)
minutos_jugados.sort()
print(minutos_jugados)
minutos_jugados.sort(reverse=True)
print(minutos_jugados)
ordenada = sorted(minutos_jugados)
print(minutos_jugados)
print(ordenada)

jugadores_mercado = [
    {"nombre": "Cristiano", "precio": 999, "stock": 5, "cat": "pro"},
    {"nombre": "Messi", "precio": 25, "stock": 20, "cat": "inferiores"},
    {"nombre": "Neymar", "precio": 450, "stock": 3, "cat": "pro"},
    {"nombre": "Mbappe", "precio": 60, "stock": 8, "cat": "inferiores"},
    {"nombre": "Haaland", "precio": 79, "stock": 0, "cat": "pro"},
]

precios = list(map(lambda p: p["precio"], jugadores_mercado))
nombres = list(map(lambda p: p["nombre"].upper(), jugadores_mercado))
print(precios)

con_stock = list(filter(lambda p: p["stock"] > 0, jugadores_mercado))
tech = list(filter(lambda p: p["cat"] == "pro", jugadores_mercado))
print([p["nombre"] for p in con_stock])

por_precio = sorted(jugadores_mercado, key=lambda p: p["precio"])
mas_caro = sorted(jugadores_mercado, key=lambda p: p["precio"], reverse=True)[0]
print(f"Más caro: {mas_caro['nombre']} ({mas_caro['precio']}€)")

total = sum(p["precio"] * p["stock"] for p in jugadores_mercado)
mas_barato = min(jugadores_mercado, key=lambda p: p["precio"])
print(f"Total inventario: {total}€")
print(f"Más barato: {mas_barato['nombre']}")

hay_sin_stock = any(p["stock"] == 0 for p in jugadores_mercado)
todos_tech = all(p["cat"] == "pro" for p in jugadores_mercado)
print(f"¿Hay sin stock? {hay_sin_stock}")
print(f"¿Todos son tech? {todos_tech}")