from functions.utils import load_cashbox, save_cashbox

def deposit_money(tipo):
    """
    Permite depositar billetes al cajero.
    Actualiza el archivo cashbox.json sumando las cantidades ingresadas.
    """
    cashbox = load_cashbox()

    print(f"\n=== DEPÓSITO DE DINERO ({tipo.upper()}) ===")
    print("Denominaciones disponibles:")
    for billete in cashbox[tipo].keys():
        print(f"- {billete} {tipo}")

    while True:
        billete = input(f"Ingrese el valor del billete que desea depositar ({tipo}): ")

        # Validar si el billete existe
        if billete not in cashbox[tipo]:
            print("❌ Billete no válido. Intente con una denominación existente.")
            continue

        try:
            cantidad = int(input(f"Ingrese cuántos billetes de {billete} va a depositar: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a cero.")
                continue
        except ValueError:
            print("Debe ingresar un número entero válido.")
            continue

        # Actualizar el saldo del cajero
        cashbox[tipo][billete] += cantidad
        save_cashbox(cashbox)

        print(f"✅ Se depositaron {cantidad} billetes de {billete} {tipo}.")
        print(f"Nuevo total de billetes de {billete}: {cashbox[tipo][billete]}")

        # Preguntar si desea continuar
        seguir = input("¿Desea depositar más billetes? (s/n): ").lower()
        if seguir != "s":
            break