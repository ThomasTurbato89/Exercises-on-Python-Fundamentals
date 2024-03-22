import random
import time

start = time.time_ns()
lista = []

for v in range(1,10000000):
    lista.append(random.randint(1, 1000000000))
end = time.time_ns()

print("il tempo richiesto per cercare è: ", (end-start)/1000000000)

start = time.time_ns()
trovati = 0
for v in range(1, 10000000):
    if random.randint(1, 1000000000) in lista:
        trovati =+ 1
end = time.time_ns()

print("il tempo richiesto per cercare è: ", (end-start)/1000000000, "e ne ha trovati", trovati)

