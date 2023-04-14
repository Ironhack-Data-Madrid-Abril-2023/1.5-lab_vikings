import random
from xml import sax
# Soldier

class Soldier:

    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health-=damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return(f"{self.name} has received {damage} points of damage")
        else:
            return(f"{self.name} has died in act of combat")
    def battleCry(self):
        return "Odin Owns You All!"
            
        
        

# Saxon


class Saxon(Soldier):
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return(f"A Saxon has received {damage} points of damage")
        else:
            return("A Saxon has died in combat")
    

# War


class War():
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        Viking = random.choice(self.vikingArmy)
        Saxon = random.choice (self.saxonArmy)
        self.damage = Viking.strength
        Saxon.receiveDamage(Viking.strength)
        if Saxon.health <= 0:
            self.saxonArmy.remove(Saxon)

        return ("A Saxon has died in combat")

    def saxonAttack (self):
        Viking = random.choice(self.vikingArmy)
        Saxon = random.choice (self.saxonArmy)
        self.damage = Saxon.strength
        Viking.receiveDamage(Saxon.strength)
        if Viking.health <= 0:
            self.vikingArmy.remove(Viking)
            return (f"{Viking.name} has died in act of combat")
        else:
            return(f"{Viking.name} has received {self.damage} points of damage")

            
        

    def showStatus(self):
        if not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        elif not self.saxonArmy:
            return "Vikings have won the war of the century!"
        else:
            return "Vikings and Saxons are still in the thick of battle."






       


