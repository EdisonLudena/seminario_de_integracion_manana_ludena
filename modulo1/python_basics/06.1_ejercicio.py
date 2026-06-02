print("Evaluacion empleados")
antiguedad =  input("Ingrese su antiguedad en la empresa: ")
calificacion_d = input("Ingrese su calificacion de desempeño: ")
salario = input("Ingrese su salario mensual: ")
if(int(antiguedad) > 1):
    if(int(calificacion_d) > 8):
        if(int(salario) < 1000):
            print("bono de $200")
        else:
            print("bono de $100")
    else:
        print("No puede optar al bono")
        
else:
    print("No aplica para este tipo de evaluacion")