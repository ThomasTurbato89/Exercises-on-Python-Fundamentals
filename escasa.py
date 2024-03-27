import json

#Per leggere un file json 
filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()


# !!!! SONO TUTTE OPERAZIONI SU LISTE !!!!
# 1) contare quanti calciatori hanno giocato per l'Italia
# 2) contare quanti calciatori hanno giocato per il Brasile
# 3) contare quanti calciatori hanno giocato per l'Argentina
# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
# 8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
#    Organizzare per nazione. Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, quale squadra francese, ...

#Esempio:
quantiCalciatori = dict()
for v in worldcup:
    # se v.Team è già presente, sommo 1, altrimenti metto a 1
    if v["Team"] in quantiCalciatori.keys():
        quantiCalciatori[v["Team"]]=quantiCalciatori[v["Team"]]+1
    else:
        quantiCalciatori[v["Team"]]=1

print(quantiCalciatori)

italiani = 0
for v in worldcup:
    if v["ClubCountry"] == "Italy":
        italiani += 1

print("Numeri italiani: ", italiani)

brasiliani = 0
for v in worldcup:
    if v["ClubCountry"] == "Brazil":
        brasiliani += 1

print("Numeri brasiliani: ", brasiliani)

Argentina = 0
for v in worldcup:
    if v["ClubCountry"] == "Argentina":
        Argentina += 1

print("Numeri argentini: ", Argentina)
Compleanno=[]
for Date in worldcup:
    yearb=Date["DateOfBirth"].split("-")[0]
    if yearb != "": 
        yearb=int(yearb)
        yearc=Date["Year"]
        Compleanno.append((yearb, yearc)) #tupla
#calcola giocatore gio. e anziano
Anno = [dates[1]-dates[0] for dates in Compleanno]

print("Calciatore più anziano:", max(Anno))
print("Calciatore più giovane:", min(Anno))

# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
#    Organizzare per nazione. Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, 
#    quale squadra francese, ...

squadre = dict()
for c in worldcup:
    if c["Club"] in squadre.keys():
        squadre[c["Club"]] += 1
    else:
        squadre[c["Club"]] = 1

print(squadre)

massimo = 0
squadra = None
for s in squadre.items():
    if s[1] > massimo:
        squadra,  massimo = s

print(massimo,squadra)