from functions import *

time = input("Syötä aika: (xxh xxmin xxsek)\n")

time = time.split(" ")
hours = time[0]
hours = int(hours[:-1])
minutes = time[1]
minutes = int(minutes[:-3])
seconds = time[2]
seconds = int(seconds[:-3])

seconds = count_seconds(hours, minutes, seconds)

print(f"Yhteensä {seconds} sekuntia.")