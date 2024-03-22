numero = ""
counter = False
while True:
    c = input("Digita 0-9,+-/=: ")
    if len(c) > 0:
        c = c[0]
    if len(c) == 0:
        continue
    if c == ",":
        if counter:
            print("non puoi mettere più di una virgola")
            continue
        counter = True

        
    # dovete leggere un numero sia intero, sia decimale
    # e stamparlo nella sua interezza quando viene
    # digitato un simbolo non numerico (+-/=)
    #
    # Terminerete quando varrà la
    if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ","]:
        # Stampate il numero letto
        print("Il numero è: ", numero)
        break
    else:
        # costruzione del numero...
        numero = numero + c