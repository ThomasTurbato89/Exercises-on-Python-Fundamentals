import math

def calcola_ipotenusa(cateto1, cateto2):
    ipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    return ipotenusa

def calcola_distanza():
    λ1 = math.radians(10.8)
    λ2 = math.radians(-123.1)
    ϕ1 = math.radians(59.9)
    ϕ2 = math.radians(49.3)
    r = 6371

    distanza = 2*r*math.asin(math.sqrt(math.sin(1/2*(ϕ2-ϕ1))**2 + math.cos(ϕ1) * math.cos(ϕ2) * math.sin(1/2*(λ2-λ1))**2))
    return distanza


if __name__ == "__main__":
    cateto1 = float(input("Inserisci la lunghezza del primo cateto: "))
    cateto2 = float(input("Inserisci la lunghezza del secondo cateto: "))
    
    ipotenusa = calcola_ipotenusa(cateto1, cateto2)
    print("L'ipotenusa è:", ipotenusa)

    distanza = calcola_distanza()
    print("La distanza tra Oslo e Vancouver è:", distanza)