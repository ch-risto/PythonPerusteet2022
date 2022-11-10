# pyydetään teksti käyttäjältä
text = input("Anna jokin teksti:\n")

# käänteinen teksti
reversed_text = text[::-1]

# tulostetaan käänteinen teksti
print(reversed_text)

# jos teksti on tyhjää
if text =="":
    print("Antamasi teksti on tyhjä")

# jos teksti ja käänteinen teksti ovat samat, kyseessä on palindromi
elif text == reversed_text:
    print("Palindromi: KYLLÄ")

else:
    print("Palindromi: EI")
