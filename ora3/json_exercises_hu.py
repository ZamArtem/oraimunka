import json
    
    
def megnyit(file):
    with open(file,"r")as j:
        x = json.load(j)
    return(x)

data = megnyit("valami.json")


print(data["persons"])


"""
2. Feladat: JSON adat módosítása és mentése
   Leírás: Készíts egy programot, amely betölt egy JSON fájlt, módosít benne egy kulcs értékét, majd elmenti az adatot egy új fájlba.
   Lépések:
      - Nyisd meg a JSON fájlt olvasásra és töltsd be az adatokat.
      - Módosíts egy megadott kulcs értékét.
      - Írd vissza az adatokat egy új JSON fájlba.
"""

def modosit(modositott_nev,file,szam,nev):
    data = megnyit(file)
    
    data["persons"][szam]["name"] = nev
    
    with open(modositott_nev + file, "w") as j:
        files = j.write(json.dumps(data,indent=4))
        
    return files
modosit("egy","valami.json",1,"Elek")
data = megnyit("modositott_valami.json")

print(data["persons"])

"""
3. Feladat: JSON adat szűrése
   Leírás: Írj egy programot, amely betölt egy JSON fájlt, amely egy személyek listáját tartalmazza, majd szűrd ki azokat, akik egy adott városban élnek.
   Lépések:
      - Töltsd be a JSON fájlt, amely személyeket tartalmaz.
      - Használj listakomprehensziót vagy filter függvényt a szűréshez.
      - Írasd ki az eredményt.
"""

def hely(varos,file):
    data = megnyit(file)
    x = [sor for sor in data["persons"] if varos in [sor for sor in data["persons"]]]
    return x

asd = hely("Budapest","valami.json")

print(asd)    










    