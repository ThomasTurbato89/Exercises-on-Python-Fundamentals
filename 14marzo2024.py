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
    l1.extend   
    (l.strip().split(" "))

linee = l1

print(linee)