def stringtodigitstolist(sd):
    c = list(sd)
    return c

str = "123"
print(str)
print(stringtodigitstolist(str))
"""
fin = open("alice.txt", "r")
linee = fin.readlines()
fin.close()
print(linee)

l1 = []
for l in linee:
    l1.append(l.strip())

linee = l1
print(linee)

s = "alpha;beta;gamma"
print(s.split(";"))
"""
fin = open("alice.txt", "r")
linee = fin.readlines()
fin.close()

l1 = []
for l in linee:
    l1.extend(l.strip().split(" "))

linee = l1

print(linee)

def maiuscola(c):
    return c.isupper()

l = [1,2,3,4,5,6,7,8,9,10,11,12]

def pari(n):
    return n % 2 == 0

print(list(filter(pari, l)))

ls = ["uno", "", "due", "tre", "", "", "", "", "", "", "fine"]

def nonvuota(s):
    return len(s) != 0

print(list(filter(nonvuota, ls)))

fin = open("alice.txt", "r")
data = fin.read()
print("Caratteri totali: ", len(data))
fin.close()

fin = open("alice.txt", "r")
data = fin.read().replace(" ", "")
print("Caratteri senza spazi bianchi: ", len(data))
fin.close()

fin = open("alice.txt", "r")
data = fin.read()
fin.close()

alfanum = 0
for c in data:
    if c.isalnum():
        alfanum += 1

print("I caratteri alfanumerici sono: ", alfanum)