# tuodaan tarvittava lisämoduuli datetime (iän laskemista varten) colorama
# ja sieltä Fore, jolla teksin väriä saadaan muokattua
from colorama import Fore, Style
from datetime import date

# Luodaan hyvikseen muuttuja henkilöiden määrälle,
# jotta muokkaaminen tulevaisuudessakin olisi suoraviivaista.
# Luodaan muuttuja myös syntymävuosille ->
# kerätään käyttäjältä pyydetyt tiedot sinne,
# sekä kysytylle vuodelle että nykyiselle vuodelle

person = 5
years = []
year = 0
current_year = date.today().year

# Kysytään silmukassa käyttäjältä viiden
# eri henkilön syntymävuodet.
for n in range(person):
    year = int(input(f"Anna henkilön {n+1} syntymävuosi:\n"))
    years.append(year)

# Käydään silmukassa läpi jokainen vuosiluku
for n in years:

    # lasketaan henkilön ikä
    age = current_year - n

    # Jos ikä on sallituissa rajoissa:
    if age > 0 and age < 125:
        print(Fore.GREEN + f"{age} vuotta, Ikä OK!." + Style.RESET_ALL)

    else:
        print(Fore.RED + f"{age} vuotta, ikä ei ole oikeassa muodossa." + Style.RESET_ALL)

    # Palautetaan lopuksi muotoilu normaaliksi
    # print(Style.RESET_ALL)

print("Valmis!")