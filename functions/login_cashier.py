def login():
    print("=== INICIO DE SESIÓN DEL CAJERO ===")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    if usuario == "ppjuares" and contraseña == "1234":
        print(" Inicio de sesión exitoso.\n")
        return True
    else:
        print(" Usuario o contraseña incorrectos.\n")
        return False