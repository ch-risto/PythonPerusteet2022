# Pyydetään käyttäjä määrittelemään lukualue
min = int(input("Anna alueen alaraja:\n"))
max = int(input("Anna alueen yläraja:\n"))

# luodaan muuttuja, jonka arvoa verrataan silmukan sisällä
number = min - 1
# luodaan silmukka, jossa, käydään läpi jokainen luku määritelmän sisällä
for n in range((max+1)-min):
    number = number + 1

    # testataan numeroa: jos luku on jaollinen viidellä, testataan onko se jaollinen seitsemällä,
    # muussa tapauksessa jatketaan hakua. Kun luku löytyy, lopetetaan haku
    if number % 5 == 0:
        if number % 7 == 0:
            print(f"Luku {number} on jaollinen 5:llä ja 7:llä.")
            print("Lopetetaan haku")
            break

        else:
            print(f"{number} ei ole jaollinen seitsemällä, hylätään.")

    else:
        print(f"{number} ei ole jaollinen viidellä, hylätään.")

    if number == max:
        print("Alueelta ei löytynyt sopivaa arvoa.")