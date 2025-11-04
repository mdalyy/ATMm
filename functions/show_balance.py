from functions.utils import load_cashbox

def show_balance(tipo):
    cashbox = load_cashbox()
    print(f"\n=== SALDO DEL CAJERO ({tipo.upper()}) ===")
    total = 0
    for billete, cantidad in cashbox[tipo].items():
        subtotal = int(billete) * cantidad
        total += subtotal
        print(f"Billetes de {billete}: {cantidad} unidades -> {subtotal} {tipo}")
    print(f"TOTAL: {total} {tipo}\n")