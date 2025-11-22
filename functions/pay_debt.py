deuda = 1200

def pay_debt():
    global deuda
    print(f"\nDeuda actual: S/{deuda}")

    monto = int(input("Ingrese monto a pagar: "))

    if monto <= 0:
        print("Monto inválido.")
        return

    if monto > deuda:
        print("El monto supera la deuda.")
        return

    deuda -= monto
    print(f"Pago exitoso. Nueva deuda: S/{deuda}")