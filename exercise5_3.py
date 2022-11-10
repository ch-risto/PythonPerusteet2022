# tuodaan matikkakirjasto, koska sieltä tarvitaan pii ympyrän pinta-alan laskemiseen
import math

# koska käyttäjä saa itse päättää, koska lopettaa ohjelman, luodaan boolean, jonka ollessa totta
# ohjelma jatkuu
again = True

while again:
    # kysytään käyttäjältä ympyrän säde
    radius = float(input("Anna säde:\n"))

    # lasketaan ympyrän pinta-ala: A = πr^2
    A = math.pi * radius**2
    A = round(A, 2)

    # Tulostetaan vastaus:
    print(f"Ympyrän pinta-ala: {A}")

    # Kysytään, vieläkö käyttäjä haluaa jatkaa:
    answer = input("Haluatko jatkaa? (k/e)\n")

    if answer == "k" or answer == "K":
        again = True
    else:
        again = False
