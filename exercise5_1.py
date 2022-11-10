# a) toteuta ohjelma, joka tulostaa luvut 1-50 allekkain
# käytä while -toistolausetta

x = 0

while x < 50:
    x = x + 1
    print(x)

# b) toteuta ohjelma, joka tulostaa luvut 1-50 allekkain
# käytä for -toistolausetta

for x in range(50):
    print(x + 1)

# c) tee silmukka joka laskee kaikkien numeroiden summan väliltä 1-30
# tulosta ainoastaan lopputulos!

total = 0

for x in range(30+1):

    total = x + total

print(f"Summa:{total}")

# d) tee silmukka, joka tulostaa kaikki vuosiluvut väliltä 2005-2010
# välilyönnillä eroteltuna _samalle_ riville.

#luodaan tyhjä muuttuja
text = ""

# jotta saadaan myös vuosi 2010 mukaan, pyydetään arvot siihen +1 asti
# luodaan string text, johon kerätään kaikki pyydetyt vuodet
for year in range(2005, 2010+1):
    text = text + str(year) + " "

print(text)