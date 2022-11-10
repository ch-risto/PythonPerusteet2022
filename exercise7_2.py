fruits = [
    'apple',
    'pear',
    'banana'
]
berries = [
    'strawberry',
    'blueberry',
    'blackberry'
]
vegetables = [
    'carrot',
    'kale',
    'cucumber'
]

inventory = [fruits, berries, vegetables]

# Käydään läpi jokainen kategoria
for category in inventory:
    # käydään läpi asia kategoriassa ja tulostetaan se
    for item in category:
        print(item)