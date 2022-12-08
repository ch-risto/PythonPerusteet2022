from functions import *

# pyydetään käyttäjää syöttämään aika
time = input("Syötä aika: (xxh xxmin xxsek)\n")

# muutetaan syötetty aika tunneiksi minuuteiksi ja sekunneiksi funktiota varten
# codepost vaati version, jossa funktioon syötettiin kolme arvoa, alunperin tämä
# osa oli funktiossa
time = time.split(" ")
hours = time[0]
hours = int(hours[:-1])
minutes = time[1]
minutes = int(minutes[:-3])
seconds = time[2]
seconds = int(seconds[:-3])

# kutsutaan funktio
seconds = count_seconds(hours, minutes, seconds)

# tulostetaan vastaus
print(f"Yhteensä {seconds} sekuntia.")