def MCD(a, b):
    while(b != 0):
        R=a%b
        a=b
        b=R
    return a

a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))
 
print("Il massimo comun divisore di ", a, " e ", b, " è ", MCD(a, b))
