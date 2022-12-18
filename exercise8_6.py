# Graafinen käyttöliittymä
# Tehdään käyttöliittymä käyttämällä Tkinteriä, joten tuodaan se ohjelmaan
from tkinter import *

# Luodaan pääikkuna, sille otsikko ja taustaväri
root = Tk()
root.title("Harjoitus 8_6")
root.configure(bg="#A1BBC4")

# tehdään funktio näppäimille, jos painetaan "equal"-näppäintä, lasketaan syötetyt summat yhteen,
# jos "shut down"-näppäintä, sammutetaan ohjelma
def myClick(args):
    if args == "equal":
        sum = int(num1.get()) + int(num2.get()) + int(num3.get())
        Label(root, text=sum, bg="#A1BBC4").grid(row=5, column=2)
    if args == "shutDown":
        root.destroy()

# kokeillaan fontin tuomista - tehdään otsikolle oma fontti
font_heading = ("Helvetica", 14, "bold")

# otsikko ohjelmalle. Gridillä saadaan määriteltyä, missä mikäkin asia on
Label(root, text="Yksinkertainen laskinesimerkki", bg="#A1BBC4", font=font_heading).grid(row=1, column=1, columnspan=2, pady=5)

# Kysytään käyttäjältä tietoa entry laatikoilla.
# Laatikot ja niiden otsikot. Gridillä saadaan määriteltyä missä kohtaa pääikkunaa ne ovat
# padilla saadaan luotua väljyyttä ja bg määrittelee taustavärin
Label(root, text="Luku 1", bg="#A1BBC4").grid(row=2, column=1, padx=5)
num1 = Entry(root, width=15, bg="#E5EAEA")
num1.grid(row=2, column=2, padx=5)
Label(root, text="Luku 2", bg="#A1BBC4").grid(row=3, column=1, padx=5)
num2 = Entry(root, width=15, bg="#E5EAEA")
num2.grid(row=3, column=2, padx=5)
Label(root, text="Luku 3", bg="#A1BBC4").grid(row=4, column=1, padx=5)
num3 = Entry(root, width=15, bg="#E5EAEA")
num3.grid(row=4, column=2, padx=5)

# Otsikko sille kentälle, mihin tulos tulostetaan
Label(root, text="Tulos:", bg="#A1BBC4").grid(row=5, column=1)

# painikkeet
myButton1 = Button(root, text="Sammuta ohjelma", bg="#E1A4C4", command=lambda: myClick("shutDown"))
myButton2 = Button(root, text="Näytä tulos", bg="#E1A4C4", command=lambda: myClick("equal"))

myButton1.grid(row=6, column=1, pady=10, padx=5)
myButton2.grid(row=6, column=2, pady=10, padx=5)

# "Tulostetaan" ikkuna
root.mainloop()