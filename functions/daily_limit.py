import json
from datetime import datetime

LIMIT = 1500

def load_limits():
    with open("data/limits.json", "r") as f:
        return json.load(f)

def save_limits(data):
    with open("data/limits.json", "w") as f:
        json.dump(data, f, indent=4)

def check_daily_limit(monto):
    data = load_limits()
    hoy = datetime.now().strftime("%Y-%m-%d")

    if data["ultima_fecha"] != hoy:
        data["retiro_dia"] = 0
        data["ultima_fecha"] = hoy

    if data["retiro_dia"] + monto > LIMIT:
        print(f"Supera el límite diario de S/{LIMIT}.")
        return False

    data["retiro_dia"] += monto
    save_limits(data)
    return True