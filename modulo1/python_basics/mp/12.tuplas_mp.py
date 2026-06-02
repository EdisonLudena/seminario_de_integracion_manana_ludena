sin_lesiones = ()
id_unico_jugador = (42,)
coordenadas_gps = (3, 4)
color_equipacion = (255, 128, 0)
datos_prospecto = ("Ana", 28, "Madrid")

registro_scouting = 10, 20
print(type(registro_scouting))

print(datos_prospecto[0])
print(datos_prospecto[-1])
print(datos_prospecto[1:])

nombre_jugador, edad, ciudad = datos_prospecto
print(nombre_jugador, edad, ciudad)

primer_minuto, *resto_minutos = (1, 2, 3, 4, 5)
print(primer_minuto)
print(resto_minutos)

*inicio_goles, ultimo_gol = (1, 2, 3, 4, 5)
print(inicio_goles)
print(ultimo_gol)

def verificar_contrato(monto, duracion_anios):
    if duracion_anios == 0:
        return None, "División por cero"
    return monto / duracion_anios, None

costo_anual, error_sistema = verificar_contrato(10, 3)
if error_sistema:
    print(f"Error: {error_sistema}")
else:
    print(f"Resultado: {costo_anual:.4f}")

historial_valoraciones = {(0, 0): "origen", (1, 0): "eje X", (0, 1): "eje Y"}
print(historial_valoraciones[(0, 0)])