# Pyydetään käyttäjältä arvoja

count1 = input("Anna ensimmäinen luku:\n")
count1 = int(count1)
count2 = input("Anna toinen luku:\n")
count2 = int(count2)

# Tulosta suurempi luku

if count1 > count2:
    print(f"Suurempi luku = {count1}")
elif count1 < count2:
    print(f"Suurempi luku = {count2}")
else:
    print("Numerot ovat yhtä suuria.")