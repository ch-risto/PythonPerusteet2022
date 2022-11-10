# Kysytään käyttäjän antama rahamäärä ja ostosten hinta

money = input("Anna rahaa:\n")
money = float(money)

price = input("Ostosten hinta:\n")
price = float(price)

# Lasketaan mahdollinen vaihtoraha
moneyback = money - price
format_moneyback = "{:.1f}".format(moneyback)

# jos asiakas antaa tasarahan
if price == money :
    print("Kiitos.")

# jos asiakas antaa rahaa tarpeeksi
elif price < money :
    print(f"Kiitos. Annetaan takaisin {format_moneyback} €")

# jos rahaa on liian vähän
elif price > money :
    money2 = input("Rahat eivät riitä, anna lisää rahaa:\n")
    money2 = float(money2)

    if money + money2 == price :
        print("Kiitos.")
    elif money + money2 > price :
        moneyback2 = money + money2 - price
        format_moneyback2 = "{:.1f}".format(moneyback2)
        print(f"Kiitos. Annetaan takaisin {format_moneyback2} €")
    else :
        print("Sinulla ei ole tarpeeksi rahaa.")