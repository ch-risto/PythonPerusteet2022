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
    # lasketaan ylityökorvaus
    overtime = hours - 40
    payment_of_overtime = pay * 1.5
    salary = pay * 40 + overtime * payment_of_overtime

# Tulostetaan vastaus
format_salary = "{:.2f}".format(salary)

print(f"Viikon ansiosi ovat: {format_salary}€")