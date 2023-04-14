
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        
        self.health= health
        
        self.strength = strength
        
    def attack(self):
            
        return self.strength
    
    
    def receiveDamage(self, damage):
            
            self.health -= damage
    
        

# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        
        self.name = name
        
        self.health = health
        
        self.strenght = strength
    
    def attack(Soldier)

# Saxon


class Saxon(Soldier):
    pass

# War


class War:
    pass
