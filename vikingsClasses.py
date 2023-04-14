
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


class Viking:
    def __init__(self, name, health, strenght):
        Soldier.__init__(self,health, strenght)
        self.name=name
        

    def receiveDamage(self,damage):
        self.health-=damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage" 
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return ("Odin los posee todos")


# Saxon


class Saxon:
    pass
    def __init__(self, health, strenght):
        self.health=health
        self.strenght=strenght
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"




# War


class War:
    pass

def addViking(self, viking):
    self.vikingArmy.append(viking)

def addSaxon(self, saxon):
    self.saxonArmy.append(saxon)

def vikingAttack(self):
    saxon = self.getRandomSoldier(self.saxonArmy)
    viking = self.getRandomSoldier(self.vikingArmy)
    message = saxon.receiveDamage(viking.strength)
    if saxon.health <= 0:
        self.saxonArmy.remove(saxon)
    return message

def saxonAttack(self):
    saxon = self.getRandomSoldier(self.saxonArmy)
    viking = self.getRandomSoldier(self.vikingArmy)
    message = viking.receiveDamage(saxon.strength)
    if viking.health <= 0:
        self.vikingArmy.remove(viking)
    return message

def getRandomSoldier(self, army):
    return random.choice(army)

def showStatus(self):
    if not self.saxonArmy:
        return "Vikings have won the war of the century!"
    elif not self.vikingArmy:
        return "Saxons have fought for their lives and survive another day..."
    else:
        return "Vikings and Saxons are still in the thick of battle."


