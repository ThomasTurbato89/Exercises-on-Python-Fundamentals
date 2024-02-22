import math

def calcola_area_botte(r1, r2, r3, h):
    S1 = math.pi * r1**2
    S2 = math.pi * r2**2
    S3 = math.pi * r3**2
    
    V = h * (S1 + 4*S2 + S3)
    return V

def cm3_to_litri(volume_cm3):
    return volume_cm3 / 1000

def main():
    r1 = float(input("Inserisci il raggio del cerchio superiore (r1): "))
    r2 = float(input("Inserisci il raggio del cerchio intermedio (r2): "))
    r3 = float(input("Inserisci il raggio del cerchio alla base (r3): "))
    h = float(input("Inserisci l'altezza della botte (h): "))

    area_botte_cm3 = calcola_area_botte(r1, r2, r3, h)
    area_botte_litri = cm3_to_litri(area_botte_cm3)
    print("L'area della botte è:", area_botte_litri, "litri")

if __name__ == "__main__":
    main()