import math

sivu1 = input("Anna särmiön ensimmäisen sivun pituus:\n")
sivu1 = float(sivu1)

sivu2 = input("Anna särmiön toisen sivun pituus:\n")
sivu2 = float(sivu2)

sivu3 = input("Anna särmiön kolmannen sivun pituus:\n")
sivu3 = float(sivu3)

tilavuus = sivu1 * sivu2 * sivu3

print(f"Särmiön tilavuus: {tilavuus} m3")

radius = input("Anna pallon säde:\n")
radius = float(radius)

tilavuus2 = 4/3 * math.pi * radius**3
format_tilavuus2 = "{:.2f}".format(tilavuus2)

print(f"Pallon tilavuus: {format_tilavuus2} m3")
