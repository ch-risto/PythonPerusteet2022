# Kokoelma ravintoloista:
restaurants = {
    0: {
        'name': 'NorthDelish',
         'rating': 4.5,
         'reservations': True,
         'services': [
             'lunch',
             'dinner'],
         'price_level': 5,
         'location': 'Rovaniemi'
    },
    1: {
        'name': 'Food Galore',
         'rating': 3.8,
         'reservations': False,
         'services': [
             'breakfast',
             'lunch'],
         'price_level': 3,
         'location': 'Tornio'
    },
    2: {
        'name': 'Snacksy Oy',
        'rating': 3.2,
        'reservations': False,
        'services': [
            'lunch',
            'dinner',
            ' night'],
        'price_level': 2,
        'location': 'Oulu'
    },
    3: {
        'name': 'NorthDelish',
        'rating': 4.5,
        'reservations': True,
        'services': [
            'lunch',
            'dinner'],
        'price_level': 5,
        'location': 'Rovaniemi'
    },
    4: {
        'name': 'NorthDelish',
        'rating': 4.5,
        'reservations': True,
        'services': [
            'lunch',
            'dinner'],
        'price_level': 5,
        'location': 'Rovaniemi'
    }

}

# luodaan ämpäri ehdotuksille
suggest = []

# Kysellään käyttäjältä kysymyksiä
rate = int(input("Monenko tähden ravintolan haluat vähintään? (1-5)\n"))
price = int(input("Minkä hintatason ravintolan haluat maksimissaan? (1-5)\n"))
reservation = input("Haluatko tehdä etukäteen varauksen? (k/e)\n").lower()
time = int(input("Mihin kellonaikaan haluat ruokailla? (0-23)\n"))

# logiikka kellonaijojen suhteen:
# breakfast = 6-10
# lunch = 11-16
# dinner = 17-24
# night = 0-5

# luodaan muuttuja, jolla tarkastellaan halutaanko suositella ravintolaa
suggest = True

# luodaan silmukka, jossa käydään kaikki ravintolat läpi:
for r in restaurants:
    restaurant = restaurants[r]
    if restaurant['rating'] < rate:
        suggest = False
    if price >= restaurant['price_level']:
        suggest = False
    if reservation == 'k' and restaurant['reservations'] == False:
        suggest = False
    if time < 6 and restaurant['services'] != 'night':
        suggest = False
    elif time < 11 and restaurant['services'] != 'breakfast':
        suggest = False
    elif time < 17 and restaurant['services'] != 'lunch':
        suggest = False
    elif time <= 24 and restaurant['services'] != 'dinner':
        suggest = False
    # luodaan silmukka, jossa käydään kaikki ravintolan tiedot läpi

    if suggest:
        print(restaurant["name"])

else:
    print("Valitettavasti sopivaa ravintolaa ei löytynyt.")
