import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
        # add code here
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health -= damage
            
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength): #Tabulador con __init ya da el codigo
        super().__init__(health, strength)
        self.name = name
        self.strength = strength
    
    def  vikattack(self):
            self.attack() # Vikattack(Viking,self).attack()
            return self.strength

    def receiveDamage(self, damage):
        self.health -=damage   
        if self.health >0:
            return str(self.name) + str(' has received ') + str(damage) + str(' points of damage')
        elif self.health <= 0:
            return self.name + str(' has died in act of combat')  
    
    def battleCry(self):
        return 'Odin Owns You All!'


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength): #Tabulador con __init ya da el codigo
        super().__init__(health, strength)
        self.health = health
        self.strength = strength
    def  saxattack(self):
            self.attack() # Vikattack(Viking,self).attack()
            return self.strength
    def receiveDamage(self, damage):
         self.health -= damage
         if self.health > 0:
            return str('A Saxon has received ') + str(damage) + str(' points of damage')
         elif self.health <=0:
            return str('A Saxon has died in combat')
         

# War

class War():

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self,Viking):
            self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
            self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        sax =random.choice(self.saxonArmy)
        viki= random.choice(self.vikingArmy)
        saxonpain= sax.receiveDamage(viki.strength)
        if sax.health <= 0: self.saxonArmy.remove(sax)
        return saxonpain

    def saxonAttack(self):
        viki= random.choice(self.vikingArmy)
        sax =random.choice(self.saxonArmy)
        vikingpain = viki.receiveDamage(sax.strength)
        if viki.health <= 0: self.vikingArmy.remove(viki)
        return vikingpain

    def showStatus(self):
        if not self.saxonArmy:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'


