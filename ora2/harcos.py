"""
Feladat: Harcos játék
Készíts egy Python programot, amely egy harcos küzdelmet szimulál. A program követelményei a következők:
1. Harcos osztály
Hozz létre egy Warrior nevű osztályt, amely tartalmazza a harcos tulajdonságait és metódusait:
__init__(self, name, health, attack_power): Inicializálja a harcos nevét, életerejét és támadási erejét.
attack(self, other_warrior): Ez a metódus csökkenti az ellenfél életerejét a támadási erővel.
is_alive(self): Ez a metódus visszatér True értékkel, ha a harcos életereje nagyobb mint 0, és False-al, ha nem.
Védekezés mechanika: A harcosok védekezhetnek is, ami csökkenti a támadások által okozott sebzést.
Random sebzés: A támadások ne legyenek mindig fix erejűek, hanem véletlenszerűen változhassanak egy adott tartományon belül.
Speciális képesség: Minden harcosnak legyen egy speciális képessége, amit véletlenszerűen aktiválhatnak a csatában (pl. kritikus sebzés vagy extra védelem).
Körök számlálása: Legyen nyomon követve, hány kör után győz valaki.
2. Játékmenet
Hozz létre két harcost, akik felváltva támadják egymást, míg egyikük életereje el nem éri a nullát.
Minden körben jelenítsd meg, hogy melyik harcos támad, és mennyi életereje van az ellenfelének a támadás után.
Ha egy harcos életereje eléri a nullát, a játék véget ér, és a másik harcos nyer.
3. Hibakezelés
Használj try-except blokkokat arra az esetre, ha valamilyen váratlan hiba lépne fel a harcosok tulajdonságainak beállítása vagy a támadások során.
"""
import random
#Class
class Warrior:
    def __init__(self, name, health, attack_power):
        self.name          = name                                                             #hat ez egy nev
        self.health        = health                                                           #hp
        self.attack_power  = attack_power                                                     #attack
        self.defense_value = 0                                                                #defense stat majd a dmg-t lejjebb fogja vinni
        self.superr        = random.randint(1, 3)                                             #3 class kozott valasz (nem nincs crid dmg)
        self.stats         = f"""|name={name}|health={health}|attack_power={attack_power}|""" #statok egy helyen szepen
    # attack patern definialasa
    def attack(self, other_warrior):    
        damage = random.randint(1, self.attack_power) #random attack damage (gambling)
        #megnezzuk az a defense szamolas pld (3*0.6= 1.8)ez az 1.8 a dmg es ha (3-(0.5*3)) akkor meg mennyit blockolt (1.2) 
        if other_warrior.defense_value  > 0:
            other_warrior.health -= other_warrior.defense_value *damage
        #itt meg csak dmg van nics szivas :3
        else:
            other_warrior.health -= damage
        #printeknel nem fogok kommentelni mert azok beszelnek maguktol ;D
        print(f"{self.name} attacked {other_warrior.name} for {damage} damage. {other_warrior.name} has {round(other_warrior.health,0)} health left.")
        print({f"Attack dmg blocked {round(damage - other_warrior.defense_value *damage,2)}"if other_warrior.defense_value > 0 else 0})
        #0-ra kell allitani mert 1 korig tart a vedekezes
        other_warrior.defense_value  = 0
        #jatek veget vizsgalo cuc
        if other_warrior.health <= 0:
            print(f"{other_warrior.name} has been defeated!")
            raise SystemExit()
    #it randomizalom a defense-t (megint gambling)
    def defend(self):
        self.defense_value = round(random.uniform(0.5,0.9),2)
        print(f"Defense value: {100-self.defense_value*100}")
    #ugye a kulonleges class kepessegek (update to be continue... (nem))
    def super(self):
        if self.superr == 1:
            self.health += 50
            print(f"""{self.name} has the blessing of the warrior!(ur health is +50!)
                  {self.stats}""")
            
        elif self.superr == 2:
            self.attack_power += 15
            print(f"""{self.name} has the blessing of the ninja!(ur attack power is +14!)
                  {self.stats}""")
            
        elif self.superr == 3:
            self.health += 25
            self.attack_power += 7
            print(f"""{self.name} has the blessing of the samurai!(ur hp +25 ur attack +7)
                  {self.stats}""")
            
    def is_alive(self):
        return self.health > 0

warrior1_n = input("Enter the name of the first warrior: ")
warrior1 = Warrior(warrior1_n, random.randint(50,150), random.randint(10,30)) #mindenhol csak a "gambling"
warrior1.super()
warrior2_n = input("Enter the name of the second warrior: ")
warrior2 = Warrior(warrior2_n, random.randint(50,150), random.randint(10,30)) #mindenhol csak a "gambling" 
warrior2.super()
#round szamolo
r = 1
#fo ciklus szokasosan az egesz 1 tryban hogy ne akadjon ki
try:
    #ez folosleges de nem akarok hozza erni
    while warrior1.is_alive() and warrior2.is_alive():
        #ugye ha valaki vicces kedveben van er random dolgot ir be akkor ujra le kell futtatni szoval ez azert van(vagy miss clickel)
        while True:
            print(f"Round {r}!")
            #megnezzuk hogy el e
            if warrior2.is_alive() == True:
                a_d = input("Do you want to attack or defend? (a/d): ")
                #a = attack, d = defend
                if a_d == "a":
                    warrior1.attack(warrior2)
                    break
                elif a_d == "d":
                    warrior1.defend()
                    break
            else:
                print("Invalid input")
        #ctrl + c , ctrl + v csak a masik jatekos szamara
        while True:
            if warrior1.is_alive() == True:
                a_d = input("Do you want to attack or defend? (a/d): ")
                if a_d == "a":
                    warrior2.attack(warrior1)
                    break
                elif a_d == "d":
                    warrior2.defend()
                    break
                else:
                    print("Invalid input")
        r += 1
except ValueError:
    print(f"?????")