# Etsitään alkuluvut välillä 2-100
from colorama import Back

def checkIfPrimeNumber(number):
    prime_number = True
    # alkulukuja ovat luvut, jotka ovat jaollisia ainoastaan itsellään ja 1:llä
    # jos luku on jaollinen jollain aiemmin esiintyneellä numerolla, se ei ole alkuluku
    for i in range(2, number):
        if (number % i) == 0:
            prime_number = False
            break

    return prime_number

# Tulostetaan kaikki luvut 2-100, jos luku on alkuluku, taustaväri on vihreä, muuten punainen
for n in range(2, 101):
    if checkIfPrimeNumber(n):
        print(Back.GREEN + f" {n} ")
    else:
        print(Back.RED + f" {n} ")