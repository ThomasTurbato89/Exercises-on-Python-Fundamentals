"""
In una stanza entrano, uno dopo l'altro, 10 persone, rispettivamente:
antonio, marco, andrea, luigi, tony, bruno, laura, anita, annarita, lucia
le prime due vanno via dopo un pochino di tempo ma entrano altre tre persone
john, alice, mary
altre due vanno via, sempre in ordine di ingresso (primo entrato, primo a uscire)
stampare l'elenco delle persone presenti
"""

import random

persone = ["antonio", "marco", 'andrea', 'luigi', 'tony', 'bruno', 'laura', 'anita', 'annarita', 'lucia']

persone.pop(0)
persone.pop(0)

persone.append('john')
persone.append('alice')
persone.append('mary')

persone.pop(0)
persone.pop(0)

print("Persone prima dell'ordine ", persone)

persone.sort()

print("Persone dopo l'ordine ", persone)

numeri = []
counter = 0

while counter <= 1000000:
    numeri.append(random.randint(0, 1000000))
    counter += 1

counter = 0
somma = 0
while counter <= 1000000:
    somma = somma + numeri[counter]
    counter += 1

print("la somma del milione di numeri è: ", somma)

media = somma / 1000000
print("La media è: ", media)
