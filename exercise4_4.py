# Käytetään tehtävässä (try/except) virheenkäsittelyä.
try:
    # Pyydetään käyttäjältä kaksi eri numeroa
    num1 = int(input("Anna ensimmäinen numero:\n"))
    num2 = int(input("Anna toinen numero:\n"))

    # Tulostetaan jakolaskun tulos
    print(num1/num2)

except ValueError:
    print("Virheellinen muoto.")
except ZeroDivisionError:
    print("Nollalla ei saa jakaa.")