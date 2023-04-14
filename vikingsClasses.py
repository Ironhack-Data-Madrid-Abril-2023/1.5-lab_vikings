
# Soldier
import random

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
        self.health= health
        self.strength=strength
    def attack(self):
        return Viking.strength
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return self.name + " has received " + str(damage) + " points of damage "
        elif Viking.health <= 0:
            return self.name + " has received " + str(damage) + " points of damage "
    def battleCry(self):
        return " Odin Owns You All! "

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health= health
        self.strength=strength
    def attack(self):
        return Saxon.strength
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return " A Saxon has received " + str(damage) + " points of damage "
        elif Viking.health <= 0:
            return "A Saxon has died in combat"

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, viking):
        self.vikingArmy= []
    def addSaxon(self, saxon):
        self.saxonArmy = []
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)    
        damage = viking.attack()
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return saxon.receiveDamage(damage)
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)    
        damage = saxon.attack()
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return viking.receiveDamage(damage)
    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survived another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    


