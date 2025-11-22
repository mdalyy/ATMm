import datetime

def generate_voucher(tipo, operacion, monto):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n=== VOUCHER ===")
    print(f"Fecha: {fecha}")
    print(f"Moneda: {tipo}")
    print(f"Operación: {operacion}")
    print(f"Monto: {monto}")
    print("===================")
