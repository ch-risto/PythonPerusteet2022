# Lottorivi
import random

# tehdään funktio lottoarvonnasta
def suoritetaanLottoarvonta():
    # luodaan lista, johon numeroita kerätään ja tehdään boolean hallitsemaan numeroiden arpomista
    lottery_numbers = []
    lottery = True

    # Arvotaan numeroita niin kauan, kunnes listaan on kerätty kymmenen numeroa
    # tarkistetaan joka numeron kohdalla, ettei se ole listassa
    while lottery:
        number = random.randint(1, 40)
        if number in lottery_numbers:
            continue
        else:
            lottery_numbers.append(number)
        if len(lottery_numbers) == 10:
            lottery = False

    return lottery_numbers

# Huvinpäiten, pyydetään käyttäjältä vähän vuorovaikutusta ohjelman kanssa
draw = input("Suoritetaanko lottoarvonta? (k/e)\n").lower()
if draw == "k":
    # Arvotaan kymmenen numeron lista random numeroita väliltä 1-40
    numbers = suoritetaanLottoarvonta()

    # erotetaan arvottujen numeroiden listasta päänumerot ja lisänumerot
    main_numbers = ", ".join(map(str, numbers[0:7]))
    extra_numbers = ", ".join(map(str, numbers[-3:]))

    # Tulostetaan arvotut numerot käyttäjälle
    print(f"Loton päänumerot ovat: {main_numbers}")
    print(f"Ja lisänumerot ovat: {extra_numbers}")
    print("Onnea illan voittajille")

else:
    print("Joku toinen kerta sitten, kiitos!")