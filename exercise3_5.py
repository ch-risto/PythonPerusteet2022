# Kysytään käyttäjän pisteet:

points = input("Anna pistemäärä:\n")
points = int(points)

# Tulostetaan arvosana ja ilmoitetaan käyttäjälle jos annettu pistemäärä ei ole mahdollinen

if 0 <= points <= 50 :
    print("Arvosana: 0")
elif 51 <= points <= 60 :
    print("Arvosana: 1")
elif 61 <= points <= 70 :
    print("Arvosana: 2")
elif 71 <= points <= 80 :
    print("Arvosana: 3")
elif 81 <= points <= 90 :
    print("Arvosana: 4")
elif 91 <= points <=100 :
    print("Arvosana: 5")
else:
    print("Pistemäärä ei ole mahdollinen")