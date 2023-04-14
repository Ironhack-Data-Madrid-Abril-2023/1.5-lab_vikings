import random

# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.health = health
        self.strength = strength
        self.name = name
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return self.name+ " " + "has received"+ " " + str(damage)+ " " + "points of damage"
        else:
            return self.name+ " " + "has died in act of combat"


    def battleCry(self):
        return "Odin Owns You All!"
# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return "A Saxon has died in combat"
        elif self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        randomSaxonIndex = random.randint(0, len(self.saxonArmy)-1)
        randomVikingIndex = random.randint(0, len(self.vikingArmy)-1)
        saxon = self.saxonArmy[randomSaxonIndex]
        viking = self.vikingArmy[randomVikingIndex]
        result = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.pop(randomSaxonIndex)
        return result

    def saxonAttack(self):
        randomSaxonIndex = random.randint(0, len(self.saxonArmy)-1)
        randomVikingIndex = random.randint(0, len(self.vikingArmy)-1)
        saxon = self.saxonArmy[randomSaxonIndex]
        viking = self.vikingArmy[randomVikingIndex]
        result = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.pop(randomVikingIndex)
        return result
         
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        
        else:
            return "Vikings and Saxons are still in the thick of battle."
        