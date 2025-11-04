def change_currency():
    print("Seleccione tipo de moneda:")
    print("1. Soles")
    print("2. Dólares")
    opcion = input(">> ")

    if opcion == "1":
        return "soles"
    elif opcion == "2":
        return "dolares"
    else:
        print("Opción inválida, se mantiene en soles.")
        return "soles"
