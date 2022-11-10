# Kysytään käyttäjältä ulkolämpötila ja kosteusprosentti
temp = int(input("Mikä on ulkolämpötila?\n"))
hum = int(input("Mikä on kosteusprosentti?\n"))

# Luodaan pyydetyt Boolean-muuttujat
freezing = False
heatwave = False
raining = False
hailstorm = False

# jos lämpötila on alle 0 astetta
if temp < 0:
    freezing = True

# jos lämpötila on yli 20
elif temp > 20:
    heatwave = True

# jos kosteusprosentti on yli 80 (paitsi jos pakkasta on yli 20)
if hum > 80 and temp > -20:
    raining = True

# jos pakkasta on yli 20
elif hum > 80 and temp <= -20:
    hailstorm = True

print(f"Ulkona on {temp} astetta.")

if raining and heatwave:
    print("Kosteaa ja tukalaa.")
elif hailstorm:
    print("Sataa rakeita!")
elif freezing:
    print("Pakkasta.")
elif raining:
    print("Sataa.")
elif heatwave:
    print("Helleaalto!")
else:
    pass