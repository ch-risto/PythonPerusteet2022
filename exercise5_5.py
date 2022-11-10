# tehdään tuple suomenkielisille kuukausille:
months = ("Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", "Heinäkuu",
          "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")

# Kysytään käyttäjältä kuukauden numero
month = int(input("Anna kuukauden numero:\n")) - 1

# tulostetaan numeroa vastaava kuukausi:
print(months[month])