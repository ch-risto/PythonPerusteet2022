# Kysytään käyttäjältä aika

minuutit = input("Anna minuutit:\n")
minuutit = int(minuutit)

# Lasketaan montako tuntia (60min) minuutteihin mahtuu

tunnit = minuutit // 60

# Montako minuuttia jää jäljelle

minuutit = minuutit % 60

# Hox, voisi olla turvallisempaa käyttää jotain muuta muuttujaa kuin "minuutit" uudelleen

print(f"{tunnit}h {minuutit}min")