# Postihintalaskuri!

# Pyydetään käyttäjältä lähetyksen tyyppi ja paino

item = input("Syötä lähetyksen tyyppi: paketti/kirje\n")
weight = input("Syötä lähetyksen paino g:\n")
weight = int(weight)
price = 0
fit_to_mail = True

# erilaiset hintavariaatiot kirjeelle:

if item == "kirje":
    if weight < 200:
        price = .50

    elif 200 <= weight < 500:
        price = round(.5 + weight//100 * .04, 2)

    elif weight >= 500:
        fit_to_mail = input("Mahtuuko kirje postilaatikkoon: K/E\n")
        if fit_to_mail == "K":
            price = round(.5 + weight//100 * .07, 2)

        elif fit_to_mail == "E":
            price = round(.5 + weight//100 * .07 + 2, 2)

# erilaiset hintavariaatiot paketille:

elif item == "paketti":
    if weight < 200:
        price = 2

    elif 200 <= weight < 500:
        price = round(2 + weight//100 * .08, 2)

    elif weight >= 500:
            price = round(2 + weight//100 * .14, 2)

print(f"Hinta on {price}€")