import random

print("Tabelina del 23:")

for moltiplicando in range(11):

    print(23*moltiplicando)

numeri = []
counter = 0

while counter <= 99:
    numeri.append(random.randint(1, 10))
    counter += 1

print("100 numeri casuali da 1 a 10: ", numeri)

somma = 0
counter = 0
while counter <= 99:
    somma = somma + numeri[counter]
    counter += 1

print("La somma dei numeri casuali è: ", somma)

l_pari = []
l_dispari = []

for i in range(1001):
    if i % 2 == 0:
        l_pari.append(i)
    else:
        l_dispari.append(i)
print("Lista numeri pari: ", l_pari)
print("Lista numeri dispari: ", l_dispari)
l_tot = l_pari
for i in range(500):
    l_tot.append(l_dispari[i])

print("Lista numeri totali prima pari e poi dispari: ", l_tot)