from functions.login_cashier import login
from functions.show_balance import show_balance
from functions.pull_money import pull_money
from functions.deposit_money import deposit_money
from functions.cash_inventory import show_inventory
from functions.change_type_of_balance import change_currency

def main():
    if not login():
        return
    tipo = "soles"

    while True:
        print(f"\n=== CAJERO AUTOMÁTICO ({tipo.upper()}) ===")
        print("1. Ver saldo del cajero")
        print("2. Retirar dinero")
        print("3. Depositar Dinero")
        print("4. Ver inventario de billetes")
        print("5. Cambiar tipo de moneda (soles/dólares)")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            show_balance(tipo)
        elif opcion == "2":
            pull_money(tipo)
        elif opcion == "3":
            deposit_money(tipo)
        elif opcion == "4":
            show_inventory()
        elif opcion == "5":
            tipo = change_currency()
        elif opcion == "6":
            print("Gracias por usar el cajero. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
