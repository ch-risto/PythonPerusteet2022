# Kysytään käyttäjältä päivän lämpötila:

temperature = input("Syötä päivän lämpötila:\n")
temperature = int(temperature)

# Tulostetaan vaihtoehtoja

if 0 <= temperature <= 10:
    print("KYLMÄÄ")
elif 11 <= temperature <= 15:
    print("KOLEAA")
elif 16 <= temperature <= 20:
    print("NORMAALI LÄMPÖTILA")
elif 21 <= temperature <= 25:
    print("LÄMMINTÄ")
elif 26 <= temperature <=30:
    print("HELLETTÄ")
else:
    pass