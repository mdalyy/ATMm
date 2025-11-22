from functions.choose_account import choose_account

def transfer_money():
    origen = choose_account()
    destino = choose_account()

    if origen == destino:
        print("No puedes transferir a la misma cuenta.")
        return

    monto = int(input("Monto a transferir: "))

    print(f"Transferencia de {monto} de {origen} a {destino} realizada.")
