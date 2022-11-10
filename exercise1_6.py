sentit = input("Anna 1-100 senttiä:\n")
sentit = int(sentit)

# Montako 50snt kolikkoa summaan mahtuu?

viiskyt = sentit // 50
remViiskyt = sentit % 50

# montako 20snt kolikkoa summaan mahtuu?

kakskyt = remViiskyt //20
remKakskyt = remViiskyt % 20

# jne

kymppi = remKakskyt // 10
remKymppi = remKakskyt % 10

viis = remKymppi // 5
remViis = remKymppi % 5

kaks = remViis // 2
remKaks = remViis % 2

yks = remKaks // 1

print(f"50 snt kolikoita {viiskyt} kpl\n"
      f"20 snt kolikoita {kakskyt} kpl\n"
      f"10 snt kolikoita {kymppi} kpl\n"
      f"5 snt kolikoita {viis} kpl\n"
      f"2 snt kolikoita {kaks} kpl\n"
      f"1 snt kolikoita {yks} kpl")