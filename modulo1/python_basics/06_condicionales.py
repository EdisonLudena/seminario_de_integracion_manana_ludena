print("condicionales simples")
edad=  input("Incluye edad:")
if (int(edad)>=18):
    print("Mayor de edad")
    
print("condicionales dos caminos")
temperatura = input("Incluye temperatura: ")
if(int(temperatura)>=38):
    print("temperatura alta")
else:
    print("temperatura normal")
    
    
print("condicionales multiples")
nota = input("Incluir nota: ")
if(int(nota)>=90):
    print("Excelente")
elif(int(nota)>=80):
    print("Bueno")
elif(int(nota)>=70):
    print("Aprobado")
else:
    print("Reprobado")
    
print("condicionales if anidados")
tiene_reserva = True
dinero = 25
plato = "pizza"
if(tiene_reserva):
    if(dinero>=20):
        if(plato == "pizza"):
            print("Tu pizza cuesta $20. Pedido confirmado")
        else:
            print("Plato disponible")
    else:
        print("Dinero insuficiente")
else:
    print("No tiene reserva")