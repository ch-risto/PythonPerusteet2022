movies = [
    {'name': 'Komisario Palmun erehdys', 'year': 1960},
    {'name': 'Kauas pilvet karkaavat', 'year': 1996},
    {'name': 'Mies vailla menneisyyttä', 'year': 2002},
    {'name': 'Stand by me', 'year': 1986},
    {'name': 'Sucker Punch', 'year': 2011},
    {'name': 'American Beauty', 'year': 1999}
]

# luodaan silmukan ulkopuolelle listat, "ämpärit", uusille ja vanhoille elokuville
new_movies = []
old_movies = []

# käydään elokuvat silmukassa läpi ja
# jaotellaan ne julkaisuvuoden perusteella kahteen eri listaan
for film in movies:
    if film['year'] < 2000 :
        old_movies.append(film['name'])
    else:
        new_movies.append(film['name'])

# tehdään listoista join-komennolla samalle riville tulostuvat muuttujat
oldies = ", ".join(old_movies)
newbies = ", ".join(new_movies)

print("Seuraavat elokuvat on julkaistu 2000-luvulla:")
print(newbies)
print()
print("Seuraavat elokuvat on julkaistu ennen vuotta 2000:")
print(oldies)