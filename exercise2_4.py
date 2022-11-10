# Kysytään käyttäjältä muuttujia

km1 = input("Matka-ajon kilometrit:\n")
km1 = float(km1)

km2 = input("Kaupunki-ajon kilometrit:\n")
km2 = float(km2)

# Lasketaan kulutukset ja niiden summa sekä määrätään tuloksen tarkkuus

consumption = km1 * 0.051 + km2 * 0.075
format_consumption = "{:.2f}".format(consumption)

# Tulostetaan vastaus

print(f"Kulutus: {format_consumption} l")