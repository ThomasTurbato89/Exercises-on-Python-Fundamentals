import random

def colorecasuale():
    l_colori = ["rosso","giallo","verde", "blu", "arancio", "ciano"]
    return l_colori[random.randint(1, len(l_colori)-1)]

def generalist():
    lista=[]
    for i in range(0,10000):
        s = str(i)
        while len(s) < 4:
            s = "0" + s
            lista.append(s)
    return lista

def stringtodigitstolist(sd):
    c = list(sd)
    return c

#print("Il colore generato è: ", colorecasuale())

#print(generalist())

sd = "918357"

print(stringtodigitstolist(sd))
