print("Verificador de contraseñas")
password_ingresada = ""
password_correcta = "1234"

while password_ingresada != password_correcta:
    password_ingresada = input("Ingrese su contraseña: ")
    
    if password_ingresada == password_correcta:
        print("Bienvenido")
    else:
        print("Contraseña incorrecta. Vuelva a intentar.")