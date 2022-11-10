# Kysytään käyttäjältä tuotteen hinta
price = input("Anna hinta ilman alv:\n")

# Koska käytetään desimaaleja, muutetaan saatu tulos floatiksi
price = float(price)

# Lasketaan alv tuotteen hintaan
total = price * 1.24

# Määritetään missä muodossa tulos halutaan näyttää
format_total = "{:.2f}".format(total)

print(f"Hinta alv:n kanssa {format_total}")
