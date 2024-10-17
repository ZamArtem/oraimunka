while True:
    try:
    
        allatok = int(input("Hany allatot szeretne hozza adni? "))

        lista = []
        pontszam = []
        nev_arany = ()
        for i in range(allatok):
            nev   = str(input("Mi a neve? "))
            arany = int(input("Mennyire ananyos? "))
            nev_arany += nev,arany
            pontszam.append(arany)
            lista.append(nev_arany)
            nev_arany = ()
            
        y_n = input("Szeretned latni az adatokat?(Y/N) ")

        if y_n.lower() == "y":
            for i in lista:
                print(i)
                
        y_n = None

        """
        y_n = input("Erdekel az atlag?(Y/N)? ")

        if y_n.lower() == "y":
            print(sum(pontszam)/len(pontszam))

        """

        y_n = input("Szeretned latni az adatokat?(Y/N) ")

        if y_n.lower() == "y":
            print(f"Max: {max(pontszam)}")
            print(f"Min: {min(pontszam)}")
            
        break
    except:
        print("value error")
                
