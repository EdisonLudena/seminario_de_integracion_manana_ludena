print("condicionales simples")
edad_jugador = input("Incluye edad del prospecto:")
if (int(edad_jugador) >= 18):
    print("Jugador apto para el equipo principal (Mayor de edad)")
    
print("condicionales dos caminos")
estado_salud = input("Incluye temperatura del jugador: ")
if (int(estado_salud) >= 38):
    print("Fiebre detectada: Jugador no disponible")
else:
    print("Estado físico óptimo: Jugador disponible")
    
print("condicionales multiples")
valoracion_scouting = input("Incluir calificación del reporte de talento (1-100): ")
if (int(valoracion_scouting) >= 90):
    print("Prospecto de Élite")
elif (int(valoracion_scouting) >= 80):
    print("Buen prospecto")
elif (int(valoracion_scouting) >= 70):
    print("Prospecto Promedio")
else:
    print("Descartar prospecto")
    
print("condicionales if anidados")
contrato_activo = True
presupuesto_fichajes = 25
jugador_buscado = "Cristiano"
if (contrato_activo):
    if (presupuesto_fichajes >= 20):
        if (jugador_buscado == "Cristiano"):
            print("Cláusula de rescisión cuesta $20M. Fichaje confirmado")
        else:
            print("Jugador disponible en el mercado")
    else:
        print("Fondos del club insuficientes")
else:
    print("Sin margen de negociación")