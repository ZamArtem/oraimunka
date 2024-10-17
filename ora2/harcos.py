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
class Warrior:
    def __init__(self, name, health, attack_power):
        self.name          = name
        self.health        = health
        self.attack_power  = attack_power
        self.defense_value = 0
        self.superr        = random.randint(1, 3)
        self.stats         = f"""|name={name}|health={health}|attack_power={attack_power}|"""

    def attack(self, other_warrior):
        damage = random.randint(1, self.attack_power)
        if other_warrior.defense_value  > 0:
            other_warrior.health -= other_warrior.defense_value *damage
        else:
            other_warrior.health -= damage
        print(f"{self.name} attacked {other_warrior.name} for {damage} damage. {other_warrior.name} has {round(other_warrior.health,0)} health left.")
        print({f"Attack dmg blocked {round(damage - other_warrior.defense_value *damage,2)}"if other_warrior.defense_value > 0 else 0})
        other_warrior.defense_value  = 0
        if other_warrior.health <= 0:
            print(f"{other_warrior.name} has been defeated!")
            raise SystemExit()

    def defend(self):
        self.defense_value = round(random.uniform(0.5,0.9),2)
        print(f"Defense value: {100-self.defense_value*100}")
        
    def super(self):
        if self.superr == 1:
            self.health += 50
            print(f"""{self.name} has the blessing of the warrior!(ur health is +50!)
                  {self.stats}""")
            
        elif self.superr == 2:
            self.attack_power += 15
            print(f"""{self.name} has the blessing of the ninja!(ur attack power is +15!)
                  {self.stats}""")
            
        elif self.superr == 3:
            self.health += 25
            self.attack_power += 7
            print(f"""{self.name} has the blessing of the samurai!(ur hp +25 ur attack +7)
                  {self.stats}""")
            
    def is_alive(self):
        return self.health > 0

warrior1_n = input("Enter the name of the first warrior: ")
warrior1 = Warrior(warrior1_n, random.randint(50,150), random.randint(10,30))
warrior1.super()
warrior2_n = input("Enter the name of the second warrior: ")
warrior2 = Warrior(warrior2_n, random.randint(50,150), random.randint(10,30))
warrior2.super()

r = 1
try:
    while warrior1.is_alive() and warrior2.is_alive():
        while True:
            print(f"Round {r}!")
            if warrior2.is_alive() == True:
                a_d = input("Do you want to attack or defend? (a/d): ")
                if a_d == "a":
                    warrior1.attack(warrior2)
                    break
                elif a_d == "d":
                    warrior1.defend()
                    break
            if warrior2.is_alive() == False:
                print(f"{warrior1.name} wins!")
            else:
                print("Invalid input")
            
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
            if warrior1.is_alive() == False:
                print(f"{warrior2.name} wins!")
                

        r += 1
except ValueError:
    print(f"?????")