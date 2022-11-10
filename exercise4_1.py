# tuodaan datetime kirjasto päivämäärää varten
from datetime import date

# ohjelmassa käytettävät tiedot:
today = date.today()
date_text = today.strftime("%d.%m.%y")
name = "Testi Henkilöinen"
birth_year = 1982
balance = 1698

# tulostetaan tiedot f-stringillä
print(f"{name} ({birth_year}), saldo: {balance} €, päivitetty {date_text}.")