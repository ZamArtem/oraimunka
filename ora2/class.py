

class Dog:
    def __init__(self,nev,kor):
        self.nev = nev
        self.kor = kor
    def display_info(self):
        return self.nev,self.kor
        
        
x = Dog("sajt",9)

print(x.display_info())
        

class BankAccount:
    def __init__(self,balance):
        self.balance = balance
        
        
    def deposit(self,ertek):
        self.balance = self.balance + ertek
        return self.balance
        
    def withdraw(self,ertek):
        self.balance = self.balance - ertek
        return self.balance
        
    def get_balance(self):
        return self.balance


y = BankAccount(0)

print(y.deposit(10000))
print(y.withdraw(10000))
print(y.get_balance())
"""

3. Feladat: Diák Osztály és Átlag Számítása
    Leírás: Készíts egy Student nevű osztályt, amely tárolja a diák nevét és jegyeit, és legyen képes kiszámolni az átlagukat.

    Feladat:

    Az osztály tárolja a diák nevét és egy jegyek listáját.
    Legyen egy metódus add_grade(grade), amely hozzáad egy jegyet a listához.
    Legyen egy metódus get_average(), amely kiszámolja és visszaadja az átlagot.
    Példányosíts egy diákot, adj hozzá jegyeket, és számold ki az átlagát.

"""

class Student:
    def __init__(self,neve,jegy):
        self.jegy = [] 
        self.neve = neve
       
        
    def add_grade(self,zat):
        self.jegy.append(zat)
        return self.jegy
    def get_average(self):
        return sum(self.jegy)/len(self.jegy)
    
        
        
z = Student("asd",None)


print(z.add_grade(4))
print(z.add_grade(4))

print(z.get_average())        
        