# tuodaan statistics-moduuli lisätehtäviä varten
import statistics

# ohjelma, jolla lasketaan tilastoa luokan oppilaiden koetuloksista
# a) kysytään oppilaiden lukumäärä
count = int(input("Opiskelijoiden lukumäärä:\n"))

# luodaan lisätehtävää varten muuttuja listalle
list_of_grades = []

# b) kysytään kunkin oppilaan koearvosana silmukassa
for grade in range(count):
    grade = int(input("Anna opiskelijan arvosana:\n"))
    # Kerätään arvosanat listaan
    list_of_grades.append(grade)

# c) lasketaan keskiarvo arvosanoista ja tulostetaan se näytölle
average = round(sum(list_of_grades)/count, 1)
print(f"Keskiarvo: {average}")

# d) tulostetaan näytölle keskimääräisestä arvosanasta sanallinen arvio
if average < 1:
    print("Huono tulos")
elif 1 <= average < 2:
    print("Heikko tulos")
elif 2 <= average <3:
    print("Tyydyttävä tulos")
elif 3 <= average <4:
    print("Hyvä tulos")
elif 4 <= average <=5:
    print("Kiitettävä tulos")

# Lisätehtäviä:

# Mediaani ja moodi saadaan joukosta helposti statistics moduulin avulla
print()
print(f"Arvosanojen mediaani: {statistics.median(list_of_grades)}")
print(f"Arvosanojen moodi: {statistics.mode(list_of_grades)}")