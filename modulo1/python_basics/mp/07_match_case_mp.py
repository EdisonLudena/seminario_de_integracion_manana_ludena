print("match-case")
plan_suscripcion = input("Plan de suscripción a activar (Basico/Premium/Cancelado): ")
match plan_suscripcion:
    case "Basico":
        print("Acceso estándar activado")
    case "Premium":
        print("Acceso Pro completo activado")
    case "Cancelado":
        print("Suscripción suspendida")
    case _:
        print(f"Estado '{plan_suscripcion}' no válido en el sistema")
        
        
print("match condiciones")
goles_partido = 7
match goles_partido:
    case g if g < 0:
        print(f"{g} es un registro inválido de goles")
    case 0:
        print("Marcador en cero")
    case g if g % 2 == 0:
        print(f"{g} es una cantidad de goles par")
    case g:
        print(f"{g} es una cantidad de goles impar")