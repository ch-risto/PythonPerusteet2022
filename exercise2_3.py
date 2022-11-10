# Kysy käyttäjältä muuttujia:

salary = input("Anna kuukausipalkkasi:\n")
salary = float(salary)

tax = input("Anna veroprosenttisi:\n")
tax = float(tax)

# Lasketaan käteen jäävä osuus

taxToPay = salary * 0.01 * tax
net = salary - taxToPay

# Tulostetaan vastaus

print(f"Käteen jäävä osuus: {net} €")
print(f"Verot: {taxToPay} €")