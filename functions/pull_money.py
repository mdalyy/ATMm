from functions.utils import load_cashbox, save_cashbox

def pull_money(tipo):
    cashbox = load_cashbox()
    monto = int(input(f"Ingrese el monto a retirar en {tipo}: "))

    if monto <= 0:
        print("Monto inválido.")
        return

    disponible = sum(int(b)*c for b, c in cashbox[tipo].items())
    if monto > disponible:
        print("❌ No hay suficiente dinero en el cajero.")
        return

    for billete in sorted(cashbox[tipo].keys(), key=int, reverse=True):
        billete = int(billete)
        cantidad = min(monto // billete, cashbox[tipo][str(billete)])
        monto -= cantidad * billete
        cashbox[tipo][str(billete)] -= cantidad

    if monto == 0:
        print(" Retiro exitoso.")
    else:
        print(" No se pudo entregar el monto exacto.")

    save_cashbox(cashbox)
