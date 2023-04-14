
''' En la clase war, no consigo quitar el error en las funciones de ataque... IndexError: list index out of range
El error parece que viene produce porque las listas vacias que he creado de los dos ejercitos (self.vikingArmy y self.saxonArmy)
estan vacías, y la funcion random no se puede aplicar a una lista vacia'''
# Entiendo el error, pero no se como arreglarlo

import random # For the war random choice

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
    def __init__(self,name,health,strength):
        self.name=name
        self.health=health
        self.strength=strength
    
    def receiveDamage(self,damage):
        self.health -= damage 
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self): 
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength
    
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"  

# War

class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        random_saxon.receiveDamage(random_viking.attack())
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
            return "A Saxon has died in combat"
        else:
            return Saxon.receiveDamage(random_viking.attack())

    def saxonAttack(self):
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        random_viking.receiveDamage(random_saxon.attack())
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
            return f"R.I.P. {random_viking.name}"
        else:
            return random_viking.receiveDamage(random_saxon.attack())
    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

        

