from PIL import Image, ImageDraw, ImageFont

# Kysytään käyttäjältä silmukassa minkä värisen kortin hän haluaa
# kunnes vastaus on "oikein". Luodaan sitä varten boolean
again = True

while again:
    answer = input("Minkä värisen kortin haluat? (punainen/sininen/keltainen)\n")

    if answer == 'punainen' or answer == 'sininen' or answer == 'keltainen':
        again = False

# luodaan listat taustan ja fonttien väreistä, jotta niitä on helppo käyttää
color = {
    'punainen': (213, 60, 0),
    'sininen': (9, 4, 110),
    'keltainen': (255, 166, 62)
}

font_color = {
    'punainen': (0, 38, 0),
    'sininen': (255, 166, 62),
    'keltainen': (0, 38, 0)
}

# Piirretään kortin pohja
img = Image.new('RGB', (500, 300), color=color[answer])

# kysytään käyttäjältä minkä tekstin haluaa korttiin
word = input("Kirjoita joulutervehdys:\n")

# jos lause on yli 25 merkkiä pitkä, jatketaan toisella rivillä
if len(word) > 25:
    word = (word[0:25] + "\n" + word[25:50])

# Tehdään piirto-olio tekstille
d = ImageDraw.Draw(img)

# käytetään moodlesta ladattua fonttia ja muutetaan koko 16
font = ImageFont.truetype("arial.ttf", 16)

# 'Piirretään' syötetty teksti
d.text((50, 180), word, font=font, fill=font_color[answer])

# Piirretään kolmioita
d.polygon([(350, 160), (280, 210), (420, 210)], fill=(28, 66, 0))
d.polygon([(350, 130), (290, 180), (410, 180)], fill=(28, 86, 0))
d.polygon([(350, 100), (300, 150), (400, 150)], fill=(28, 106, 0))

# Piirretään neliö
d.rectangle([(345, 210), (355, 220)], fill=(77, 47, 0))

# Piirretään ympyrä
d.ellipse([(335, 85), (365, 115)], fill=(213, 195, 0))

# Tallennetaan kuva
img.save('picture8_3.png')

# avataan kuva
im = Image.open(r"picture8_3.png")
im.show()