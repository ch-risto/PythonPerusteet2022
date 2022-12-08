from functions import *

# Kysytään käyttäjältä osallistujalista yhtenä tekstinä
data = input("Syötä tapahtumaan osallistujat pilkulla eroteltuna:\n")

# luodaan stringistä lista erottamalla tiedot pilkun perusteella
data = data.split(",")

# otetaan mahdolliset ylimääräiset välilyönnit pois
data = [d.strip() for d in data]

# Tulostetaan lista tähän mennessä
title = "Ilmoittautumisjärjestys:"
show_numbered_list(title, data)
print()

# järjestetään data aakkosjärjestykseen
data = sorted(data)

# Tulostetaan aakkosjärjestetty lista
title = "Aakkosjärjestys etunimen perusteella:"
show_numbered_list(title, data)
print()

# Käännetään jokaisen nimen järjestys sukunimestä etunimeksi ja järjestetään
# uusi lista aakkosjärjestykseen (logiikka ja malli tehtävänannosta)
data = sorted([" ".join(reversed(d.split(" "))) for d in data])

# Tulostetaan sukunimen perusteella aakkosjärjestetty lista
title = "Aakkosjärjestys sukunimen perusteella:"
show_numbered_list(title, data)