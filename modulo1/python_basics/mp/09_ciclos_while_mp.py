lesiones_graves = 1
while (lesiones_graves <= 5):
    print(f"lesiones_graves: {lesiones_graves}")
    lesiones_graves += 1
    
print("Control de ciclo")
print("continue")
i = 1
while (lesiones_graves <= 5):
    i += 1
    if i == 3:
        continue
    print(f"lesiones_graves: {i}")
    
print("break")
i = 1
while (lesiones_graves <= 5):
    i += 1
    if i == 3:
        break
    print(f"lesiones_graves: {i}")
    
id_entrenador = int(input("Ingrese id_entrenador: "))
while id_entrenador != 0:
    print("Ingresaste: ", id_entrenador)
    id_entrenador = int(input("Ingrese id_entrenador"))
    
    
lesiones_graves = 1
while (lesiones_graves <= 5):
    print(f"lesiones_graves: {lesiones_graves}")
    lesiones_graves += 1
else:
    print("fin del ciclo")