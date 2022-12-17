# Muutetaan tilausten loppusummaa seuraavanlaisella logiikalla:

# Kokonaissummaan lisätään lopuksi postimaksu: 7,95€
# Jos kokonaissumma on yli 99€ postimaksu on 0€
# Alennuskoodilla FALL22 vähennetään ostosten kokonaissummasta 10% (Ei koske postimaksua)
# Alennuskoodilla BK2SCHOOL vähennetään kokonaissummasta 20% vain jos kyseessä on opiskelija-asiakas
# (ei koske postimaksua)
# Voidaan käyttää vain yhtä alennuskoodia
# Jos kanta-asiakas, annetaan kokonaissummasta 100 asiakaspistettä / tilaussumman alkava 10€
# Kanta-asiakkaan tilauksen loppusummasta vähennetään 5€ jokaista täyttä 1000 asiakaspistettä kohtaan
# (Mukaan otetaan myös uudesta ostoksesta tulevat uudet kanta-asiakaspisteet

# Kysytään käyttäjältä ostosten kokonaissumma (euroina), onko asiakas opiskelija tai kanta-asiakas.

total = input("Syötä ostosten kokonaissumma euroina:\n")
total = float(total)
student_ = input("Oletko opiskelija? K / E\n")
regular_ = input("Oletko kanta-asiakas? K / E\n")
campaign_code = input("Onko sinulla alennuskoodia?\n")
points = 0
student = True
regular = True
mail = 7.95

if student_ == "E":
    student = False

if student:
    total = total * .9
    if campaign_code == "BK2SCHOOL":
        total = total * .8

if campaign_code == "FALL22":
    total = total * .9

if regular_ == "E":
    regular = False

if regular:
    points = input("Kuinka paljon kanta-asiakaspisteitä sinulla on?\n")
    points = int(points)
    points = points + total // 10 * 100
    total = total - (points // 1000 * 5)

if total > 99:
    mail = 0

#Tulosta lopullinen tilauksen loppusumma postikuluineen
print(f"Loppusumma postikuluineen on {round(total + mail, 2)}€")
print(points)