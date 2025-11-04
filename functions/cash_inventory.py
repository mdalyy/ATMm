from functions.utils import load_cashbox

def show_inventory():
    cashbox = load_cashbox()
    print("\n=== INVENTARIO COMPLETO DEL CAJERO ===")
    for tipo, billetes in cashbox.items():
        print(f"\nTipo: {tipo.upper()}")
        for b, c in billetes.items():
            print(f"Billete de {b}: {c} unidades")
