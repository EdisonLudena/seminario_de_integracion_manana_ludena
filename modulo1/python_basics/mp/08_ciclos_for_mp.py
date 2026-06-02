print("Ciclo For")
clubes = ["Barcelona", "Real Madrid", "Juventus"]
for club in clubes:
    print(club)
    
print("Recorrer palabras")
for letra in "futbol":
    print(letra)
    
print("Recorrer rango")
for minuto in range(1, 6):
    print(minuto)
    
    
print("Recorrer rango configurar paso")
for dorsal in range(1, 10, 2):
    print(dorsal)
    
print("Enumerar listas")
for i, club in enumerate(clubes):
    print(i, club)
    
print("Dos listas a la vez")
jugadores = ["Messi", "Ronaldo"]
goles = [20, 25]
for jugador, gol in zip(jugadores, goles):
    print(jugador, gol)
    
print("Control de Ciclo")
print("break")
for falta in range(10):
    if falta == 3:
        break
    print(falta)

print("continue")
for cambio in range(5):
    if cambio == 2:
        continue
    print(cambio)
    

print("for anidado")
for categoria in range(3):
    for jugador_id in range(2):
        print(categoria, jugador_id)
        
print("Lista comprehension forma corta")
valores_actualizados = [precio * 2 for precio in range(5)]
print(valores_actualizados)