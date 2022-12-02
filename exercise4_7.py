# tehdään ohjelma, joka muuttaa numerot sanoiksi
# hyväksytään maksimissaan viisinumeroiset luvut

# Pyydetään käyttäjää syöttämään luku
# tehdään se silmukassa, jotta saadaan oikean lainen teksti
num = input("Syötä jokin luku: (max.5numeroa)\n")
again = True

# Luodaan dictionary numeroiden muuttamiseksi sanoiksi
# ja sanojen numeroiksi
numbers = {
    '1': 'yksi',
    '2': 'kaksi',
    '3': 'kolme',
    '4': 'neljä',
    '5': 'viisi',
    '6': 'kuusi',
    '7': 'seitsemän',
    '8': 'kahdeksan',
    '9': 'yhdeksän',
    '0': 'nolla',
    '-': 'miinus',
    'yksi': '1',
    'kaksi': '2',
    'kolme': '3',
    'neljä': '4',
    'viisi': '5',
    'kuusi': '6',
    'seitsemän': '7',
    'kahdeksan': '8',
    'yhdeksän': '9',
    'nolla': '0'
}

# Tutkitaan, että syötetty numero on sääntöjen mukainen
if num.isnumeric() and len(num) > 5 or len(num.split()) > 5:
    while again:
        num = input("yritäppä uudelleen:\n")
        if len(num.split()) <= 5 or num.isnumeric() and len(num) <= 5:
            again = False

# Jos numerot on syötetty numeroina, tulostetaan ne kirjoitettuina
if num.isnumeric():
    for n in num:
        print(numbers[n], end=" ")

# lisätehtävä: anna käyttäjän syöttää luku myös tekstinä, eli "yksi kaksi kolme"
# varmistetaan, että kirjaimet ovat pieniä ja tehdään sanoista splitillä lista
else:
    num = num.lower()
    words = num.split(" ")
    for n in words:
        # Tutkitaan, ettei kirjoitetuissa numeroissa ole kirjoitusvirheitä,
        # jos sanaa ei ole mahdollista löytää numbers-listasta, pyydetään käyttäjää
        # käynnistämään ohjlema uudelleen
        if n not in numbers:
            print("sinulla tapahtui kirjoitusvirhe, käynnistä ohjelma uudelleen")
            break
        else:
            print(numbers[n], end="")