print("Ciclo For")
frutas = ["manzana", "banana", "pera"]
for fruta in frutas:
    print(fruta)
    
print("Recorrer palabras")
for letra in "frutas":
    print(letra)
    
print("Recorrer rango")
for i in range(1,6):
    print(i)
    
    
print("Recorrer rango configurar paso")
for i in range(1,10,2):
    print(i)
    
print("Enumerar listas")
for i, fruta in enumerate(frutas):
    print(i, fruta)
    
print("Dos listas a la vez")
nombres = ["Ana", "Luis"]
edades = [20, 25]
for nombre, edad in zip(nombres, edades):
    print(nombre, edad)
    
print("Control de Ciclo")
print("break")
for i in range(10):
    if i == 3:
        break
    print(i)

print("continue")
for i in range(5):
    if i == 2:
        continue
    print(i)
    

print("for anidado")
for i in range(3):
    for j in range(2):
        print(i, j)
        
print("Lista comprehension forma corta")
cuadrados =[x**2 for x in range(5)]
print(cuadrados)