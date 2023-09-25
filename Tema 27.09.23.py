# Să se scrie un program care gestionează o listă de mașini. O mașină este reprezentată ca dicționar și conține următoarele
# chei:
# ○ id (identificator unic) - se va genera de către program (îl generați programatic)
# ○ brand
# ○ model
# ○ hp (horse power)
# ○ price

lista_masini = []
def generate_id():
    return len(lista_masini) + 1
def adauga_masina(brand, model, hp, price):
    masina = {
        'id': generate_id(),
        'brand': brand,
        'model': model,
        'hp': hp,
        'price': price
    }
    lista_masini.append(masina)
    print("Mașina a fost adăugată cu succes!")
def afiseaza_toate_masini():
    if not lista_masini:
        print("Lista de mașini este goală.")
    else:
        print("Lista de mașini:")
        for masina in lista_masini:
            print(f"ID: {masina['id']}, Brand: {masina['brand']}, Model: {masina['model']}, HP: {masina['hp']}, Preț: {masina['price']} $")

masina1 = {'brand': 'Audi', 'model': 'Q3', 'hp': 120, 'price': 10000}
masina2 = {'brand': 'Renault', 'model': 'Clio', 'hp': 100, 'price': 7000}
masina3 = {'brand': 'Dacia', 'model': 'Logan', 'hp': 80, 'price': 3000}

adauga_masina(**masina1)
adauga_masina(**masina2)
adauga_masina(**masina3)

afiseaza_toate_masini()



