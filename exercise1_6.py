cents = int(input("Anna 1-100 senttiä:\n"))

# Montako 50snt kolikkoa summaan mahtuu?

total50 = cents // 50
cents = cents % 50

# montako 20snt kolikkoa summaan mahtuu?

total20 = cents // 20
cents = cents % 20

# jne

total10 = cents // 10
cents = cents % 10

total5 = cents // 5
cents = cents % 5

total2 = cents // 2
cents = cents % 2

print(f"50 snt kolikoita {total50} kpl\n"
      f"20 snt kolikoita {total20} kpl\n"
      f"10 snt kolikoita {total10} kpl\n"
      f"5 snt kolikoita {total5} kpl\n"
      f"2 snt kolikoita {total2} kpl\n"
      f"1 snt kolikoita {cents} kpl")