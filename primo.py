import math

def calcola_ipotenusa(cateto1, cateto2):
    ipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    return ipotenusa

if __name__ == "__main__":
    cateto1 = float(input("Inserisci la lunghezza del primo cateto: "))
    cateto2 = float(input("Inserisci la lunghezza del secondo cateto: "))
    
    ipotenusa = calcola_ipotenusa(cateto1, cateto2)
    print("L'ipotenusa è:", ipotenusa)

    