#Leggere da un file (persone.txt) i nomi, cognomi e eta di un gruppo di persone. 
#organizzarli in un dizionario la cui chiave è il cognome e il cui valore è una t-upla contenente i tre valori letti.

file = open("persone.txt", "r")
linee = file.readlines()
file.close()

l1 = []

for l in linee:
    l1.extend(l.strip().split(","))

for i in range(0, len(l1), 3):
    print("Nome: ",l1[i],"Cognome: ",l1[i+1],"Età: ",l1[i+2])

dizionario = dict()

for v in linee:
    persona = v.split(",")
    dizionario[persona[1]] = (persona[0], persona[1], persona[2])

print(dizionario)

for e in dizionario:
    print("Key: ", e, "Value: ", dizionario[e])