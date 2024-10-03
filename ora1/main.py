while True:
    try:
        diak_hoz = int(input("Hany felhasznalot? "))
        diakok = []
        jegyek = []
        for i in range(diak_hoz):
            diak_nev   = str(input("Diak neve: "))
            diak_jegye = int(input("Diak jegye: "))
            if diak_nev == "" or diak_jegye == "" or diak_jegye > 5 or diak_jegye < 1:
                raise Exception("Nem lehet ures")
            jegyek.append(diak_jegye)
            diak = (diak_nev,diak_jegye)
            diakok.append(diak)
        y_n = input("Megszeretned e tekinteni a diakokat(y/n)? ")
        if y_n == "y":
            for i in diakok:
                print(i)
        else:
            pass
        atlag = input("Szeretne tudni az atlagot(y/n)? ")
        if atlag == "y":
            avg = 0
            for i in jegyek:
                avg += i
            print(avg/len(jegyek))
        else:
            pass
        min_max = input("Szeretne tudni az min/max-ot(y/n)? ")
        if min_max == "y":
            print(f"MAX : {max(jegyek)}")
            print(f"MIN : {min(jegyek)}")
        else:
            pass
        delete = input("Elszeretne tavolitani diakot(y/n)? ")
        if delete == "y":
            diak_del = input("Diak neve: ")
            db = 0
            for i in diakok:
                for x in i:
                    if x == diak_del:
                        diakok.pop(db)
                db += 1
        else:
            pass
        for i in diakok:
                print(i)
        break
    except:
        print("Rosz input")

