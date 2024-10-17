"""
4. Feladat: Lista elem lekérése index alapján
    Leírás: Készíts egy programot, amely egy listából kér le elemeket egy megadott index alapján.
    Kérj be egy indexet a felhasználótól, és próbáld meg kiolvasni az adott indexű elemet a listából.
    Ha az index kívül esik a lista határain, kezelje a program a hibát.
"""
try:
    x = int(input("elso szam? "))
    y = int(input("masodik szam? "))
    print(x/y)
except ZeroDivisionError:
    print("0-val osztani ember ????")
    
    
try:
    z = int(input("Kerek egy szamot? "))
except:
    print("Szamot kertem ember!!! ")
    
try:
    with open("data.txt","r",encoding = "latin2")as f:
        lista = []
except:
    print("Nincs ilyen file")
    
