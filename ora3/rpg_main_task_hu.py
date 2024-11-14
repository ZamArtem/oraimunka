"""
Fő Feladat: RPG Karakterkezelő Program

Leírás: Írj egy programot, amely egy RPG (szerepjáték) karakterekből álló JSON fájlt használ. 
A program töltse be a karaktereket, majd hozzon létre belőlük Python objektumokat. A karakterek különböző tulajdonságokkal rendelkeznek, 
mint például név, szint, életerő, támadóerő és védekezés.

Cél: A karakterek használatával tudj szimulálni egy egyszerű harcot.
"""
import random
import json

with open("valamixd.json")as j:
    data = json.load(j)
    players = data["characters"]

print(players)
"""
2. Hozz létre egy Character osztályt:
   - Minden karaktert egy Character osztály reprezentáljon.
   - Az osztály tartalmazza a következő attribútumokat: név, szint, életerő, támadóerő, védekezés.
   - Implementálj egy take_damage metódust, amely csökkenti a karakter életerejét egy adott sebzés alapján.
"""
class Character:
    def __init__(self,name,level,health,attack,defense):
        self.name     = name
        self.level    = level
        self.health   = health
        self.attack   = attack
        self.defense  = defense
        self.is_alive = True
        
    def dmg(self,egy,ketto):
        damage = egy.attack - ketto.defense
        ketto.health -= damage
        print(egy.name,egy.level,egy.health,egy.attack,egy.is_alive)
        print(ketto.name,ketto.level,ketto.health,ketto.attack,ketto.is_alive)
    
        if ketto.health <= 0:
            ketto.is_alive = False
            print("Player "+ ketto.name + " dead!")
   
        return ketto.health
        
        
emberek = [Character(**sor) for sor in players]

char1 = emberek[0]
char2 = emberek[1]
char3 = emberek[2]



         
    

def fight(valaki,masvalaki):
    valaki.dmg(valaki,masvalaki)
    

    


x = random.randint(1,3)
y = None
,00    x = char1
    y = char2
if x == 2:
    x = char2
    y = char3
if x == 3:
    x = char3
    y = char1



while x.is_alive == True and y.is_alive == True:
    fight(x,y)
    

print(x.name,x.level,x.health,x.attack,x.is_alive)
print(y.name,y.level,y.health,y.attack,y.is_alive)

