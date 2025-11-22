def choose_account():
    print("\n=== SELECCIONE TIPO DE CUENTA ===")
    print("1. Ahorros")
    print("2. CTS")
    print("3. Cuenta corriente")
    print("4. Tarjeta de crédito")

    opcion = input("Opción: ")

    cuentas = {
        "1": "ahorros",
        "2": "cts",
        "3": "corriente",
        "4": "credito"
    }

    return cuentas.get(opcion, None)