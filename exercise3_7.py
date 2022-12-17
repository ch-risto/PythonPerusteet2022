# Postihintalaskuri!
def countMailingCost(item, weight, large_letter):
    # luodaan apumuuttuja painon hintakertoimelle
    weight_factor = 0
    price = 0

    # Erilaiset hintavariaatiot kirjeelle
    if item == "kirje":
        price = 0.5

        if weight >= 500:
            weight_factor = 0.07

            # Jos ei mahdu postilaatikkoon, lisätään hintaan kaksi euroa
            if largeLetter:
                price = price + 2

        if weight >= 200:
            weight_factor = 0.04

    # erilaiset hintavariaatiot paketille:
    elif item == "paketti":
        price = 2

        if weight >= 500:
            weight_factor = 0.14

        elif weight >= 200:
            weight_factor = 0.08

    # lasketaan hinta: tyyppikohtainen perusmaksu plus tyypin ja painoluokan mukaan
    # määräytyvä lisämaksu per 100g
    price = price + weight // 100 * weight_factor

    return round(price, 2)


# Pyydetään käyttäjältä lähetyksen tyyppi ja paino
item = input("Syötä lähetyksen tyyppi: paketti/kirje\n").lower()
weight = int(input("Syötä lähetyksen paino g:\n"))
large_letter = False
if item == "kirje" and weight >= 500:
    fit_to_mail = input("Mahtuuko kirje postilaatikkoon: K/E\n").upper()
    if fit_to_mail == "E":
        large_letter = True

price = countMailingCost(item, weight, large_letter)
print(f"Hinta on {price}€")