
import random

def GeneraLista(N):
    ls = []
    for i in range(N):
        ls.append(random.randint(1, N))
    return ls

def ContaUguali(ls, lsCheck):
    counter = 0
    for i in range(len(ls)):
        if ls[i] == lsCheck[i]:
            counter += 1
    return counter

def Conta(ls, lsCheck):
    counter_diverso = 0
    counter_uguale = 0
    for i in range(len(lsCheck)):
        if lsCheck[i] == ls[i]:
            counter_uguale += 1
            ls[i] = None
            lsCheck[i] = None

    for i in range(len(lsCheck)):
        for j in range(len(lsCheck)):
            if lsCheck[i] == ls[j]:
                counter_diverso += 1
                temp = ls[j]
                for h in range(len(ls)):
                    if ls[h] == temp:
                        ls[h] = None
    return counter_uguale, counter_diverso
    



n = random.randint(0, 9)
ls = [1, 2, 3]
lsCheck = [3, 1, 3]
print(ls)
print(lsCheck)

print(ContaUguali(ls, lsCheck))

print(Conta(ls, lsCheck))