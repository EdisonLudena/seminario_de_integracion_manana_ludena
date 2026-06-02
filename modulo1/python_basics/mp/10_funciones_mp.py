print('Funciones de python')
print('Funcion basica')

def inicializar_sistema():
    print('Hola desde el club de fútbol')

inicializar_sistema()


print('Funcion con parametros')
def registrarJugadorConNombre(nombre_completo):
    print(f'Jugador: {nombre_completo} ¿está listo para el entrenamiento?')

registrarJugadorConNombre('Danna')
registrarJugadorConNombre('Maria')

print('Funcion que devyelve valor con return')
def calcular_goles_totales(goles_inferiores, goles_pro):
    return goles_inferiores + goles_pro

print(calcular_goles_totales(5,6))

print('Funcion con valor por posicion')
def asignar_entrenador(nombre, edad, ciudad):
    print(f'{nombre},{edad}, {ciudad}')
asignar_entrenador('Danna', 26, 'Quito')  
asignar_entrenador(ciudad='guayaquil', nombre='Juan', edad=40) 

print('Funcion con valor por defecto')
def generar_reporte_scouting(nombre_jugador, plan="Basico", estado="Activo"):
    print(f'{plan}, {nombre_jugador} {estado}')
generar_reporte_scouting('Danna', "Premium", "Cancelado")  
generar_reporte_scouting("Juan", estado="Cancelado")
generar_reporte_scouting("Carlos", "Premium")



print('Funcion parametros posicionales')
def registrar_minutos_jugados(*minutos):
    print(f"argumentos recibidos: {minutos}")
    return sum(minutos)

print(registrar_minutos_jugados(1,2,3))
print(registrar_minutos_jugados(1,2,3,4,5,6,7))
print(registrar_minutos_jugados(10,20,22))


print('Funcion parametros combinados con posicional')
def mostrar_plantilla(nombre_entidad, *jugadores):
    print(f"argumentos recibidos: {nombre_entidad}, {jugadores}")
    print(nombre_entidad)
    for jugador in jugadores:
        print(f"  - {jugador}")
    
mostrar_plantilla("Inferiores", "naranja", "piña", "melon", "manzana")

print('Funcion parametros con clave valor variables')
def crear_perfil_jugador(**detalles):
    print(f"argumentos recibidos: {detalles}")
    for clave, valor in detalles.items():
        print(f" {clave}: {valor}")
    
crear_perfil_jugador(nombre="Danna", apellido="Gonzalez", edad=20, ciudad="Quito")


print("Funcion parametros comnbinacion de todos los tipos")
def configurar_ficha_tecnica(posicion_id, *lesiones, esta_disponible=False, **metricas):
    print(f"Host: {posicion_id}")
    print(f"Puerto: {lesiones}")
    print(f"Debug: {esta_disponible}")
    print(f"opciones: {metricas}")

configurar_ficha_tecnica("localhost", 80, 443, 8080, debug=True, timeout=30, ssl=True)

print("Devolver multiples valores")
def obtener_rango_precios(precios_fichajes):
    return min(precios_fichajes), max(precios_fichajes)

minimo, maximo = obtener_rango_precios([3,5,7,2,8,9])
print(f"El valor máximo es: {maximo}, el valor mínimo es: {minimo}")
_, maximo = obtener_rango_precios([12,13,16,24,100])
print(f"Solo maximo {maximo}")


print("Devolver un diccionario en el caso de muchos valores")
def analizar_rendimiento(estadisticas_partido):
    total = sum(estadisticas_partido)
    n = len(estadisticas_partido)

    return {
        "total": total,
        "media": total/n if n >0 else 0,
        "minimo": min(estadisticas_partido) if estadisticas_partido else None,
        "maximo": max(estadisticas_partido) if estadisticas_partido else None,
        "count": n
    }
datos = [12,88,44,55,23,45]
stats = analizar_rendimiento(datos)
print(f"Total: {stats['total']}")
print(f"Media: {stats['media']:.2f}")
print(f"Rango: {stats['minimo'] - stats['maximo']}")

print("funciones lambda")

def calcular_valor_actual(valor_inicial):
    return valor_inicial * 2
actualizar_precio_lambda = lambda valor_inicial: valor_inicial * 2
print(calcular_valor_actual(2))
print(actualizar_precio_lambda(2))

sumar_goles = lambda a, b: a + b
print(sumar_goles(5,4))