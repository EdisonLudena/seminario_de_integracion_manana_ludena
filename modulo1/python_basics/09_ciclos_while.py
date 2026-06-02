contador = 1
while(contador<=5):
    print(f"contador: {contador}")
    contador+=1
    
print("Control de ciclo")
print("continue")
i=1
while(contador<=5):
    i+=1
    if i==3:
        continue
    print(f"contador: {i}")
    
print("break")
i=1
while(contador<=5):
    i+=1
    if i == 3:
        break
    print(f"contador: {i}")
    
numero = int(input("Ingrese numero: "))
while numero!=0:
    print("Ingresaste: ", numero)
    numero=int(input("Ingrese numero"))
    
    
contador = 1
while (contador<=5):
    print(f"contador: {contador}")
    contador+=1
else:
    print("fin del ciclo")
    
    