from functions.login_cashier import login
from functions.show_balance import show_balance
from functions.pull_money import pull_money
from functions.deposit_money import deposit_money
from functions.cash_inventory import show_inventory
from functions.change_type_of_balance import change_currency
from functions.choose_account import choose_account
from functions.daily_limit import check_daily_limit
from functions.pay_debt import pay_debt
from functions.transfer import transfer_money
from functions.voucher import generate_voucher
from functions.date_utils import get_datetime


def main():
    if not login():
        return

    tipo = "soles"
    cuenta = "ahorros"

    while True:
        print(f"\n=== CAJERO AUTOMÁTICO ({tipo.upper()}) - Cuenta: {cuenta.upper()} ===")
        print("1. Ver saldo del cajero")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Ver inventario de billetes")
        print("5. Cambiar tipo de moneda (soles/dólares)")
        print("6. Elegir tipo de cuenta")
        print("7. Verificar límite diario")
        print("8. Pagar deuda")
        print("9. Transferir dinero")
        print("10. Generar comprobante")
        print("11. Ver fecha y hora actual")
        print("12. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            show_balance(tipo)

        elif opcion == "2":
            if check_daily_limit():
                pull_money(tipo)

        elif opcion == "3":
            deposit_money(tipo)

        elif opcion == "4":
            show_inventory()

        elif opcion == "5":
            tipo = change_currency()

        elif opcion == "6":
            cuenta = choose_account()

        elif opcion == "7":
            check_daily_limit(show_msg=True)

        elif opcion == "8":
            pay_debt()

        elif opcion == "9":
            transfer_money(tipo)

        elif opcion == "10":
            operacion = input("Ingrese la operación realizada: ")
            monto = input("Ingrese el monto de la operación: ")
            generate_voucher(tipo, operacion, monto)

        elif opcion == "11":
            print(f"\nFecha y hora actual: {get_datetime()}")

        elif opcion == "12":
            print("Gracias por usar el cajero. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
