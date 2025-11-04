import json

def load_cashbox():
    with open("data/cashbox.json", "r") as file:
        return json.load(file)

def save_cashbox(cashbox):
    with open("data/cashbox.json", "w") as file:
        json.dump(cashbox, file, indent=4)
