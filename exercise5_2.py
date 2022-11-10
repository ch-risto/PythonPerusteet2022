# luodaan muuttuja total
total = 0

# Kysytään käyttäjältä kuukauden sademäärä 12 kertaa silmukassa
for rain in range(12):
    rain = input("Anna kuukauden sademäärä:\n")
    rain = float(rain)
    total = rain + total

# lasketaan keskiarvo total / kuukausien määrällä
average = total / 12
average = round(average, 1)

print(f"Vuoden keskiarvo on n. {average} mm")
