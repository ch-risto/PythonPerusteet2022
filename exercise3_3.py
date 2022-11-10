# Kysytään käyttäjältä työtunnit ja palkka

hours = input("Syötä viikon työtunnit:\n")
hours = float(hours)

pay = input("Syötä tuntipalkkasi:\n")
pay = float(pay)

# Viikkoansiot ovat hours * pay
# Ylitöistä (vain ylimeneviltä tunneilta) maksetaan 50% korotus tuntipalkkaan

if hours <= 40:
    salary = pay * hours
else:
    salary = hours * pay + (hours - 40) * pay * .5

# Tulostetaan vastaus
format_salary = "{:.1f}".format(salary)

print(f"Viikon ansiosi ovat: {format_salary}€")