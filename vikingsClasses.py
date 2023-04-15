
import random

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
        self.name=name
        self.health=health
        self.strength=strength

    def receiveDamage(self, damage):
        self.health-=damage

        if self.health <= 0:
            return f'{self.name} has died in act of combat'
        else:
            return f'{self.name} has received {damage} points of damage'
    
    def battleCry():
        return 'Odin Owns You All!'


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def receiveDamage(self, damage):
        self.health-=damage
    
        if self.health <= 0:
            return f'A Saxon has died in combat'
        else:
            return f'A Saxon has received {damage} points of damage'

    

# War


class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        sax = random.choice(self.saxonArmy)
        vik = random.choice(self.vikingArmy)
        result_v = sax.receiveDamage(vik.strength)
        if sax.health <= 0:
            self.saxonArmy.remove(sax)
        return result_v
    
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result_s = viking.receiveDamage(saxon.strength)

        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result_s
     
    def showStatus(self):

        if  len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'
            



        