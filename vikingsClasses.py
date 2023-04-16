
# Soldier

import random

class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name
    
    def receiveDamage(self,damage):
        self.health -= damage
        if (self.health > 0):
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    def battleCry(self):
        return 'Odin Owns You All!'
    

# Saxon


class Saxon(Soldier):
  
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
        
    def receiveDamage(self,damage):
        self.health -= damage
        if (self.health > 0):
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'

# War


class War:
    
    
    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self,viking):
        
        self.vikingArmy.append(viking)
  
    def addSaxon(self,saxon):
        
        self.saxonArmy.append(saxon)
        
    def vikingAttack(self):
        
        n= random.randint(0,len(self.saxonArmy)-1)
        s= random.randint(0,len(self.vikingArmy)-1)
        
        self.saxonArmy[n].receiveDamage(self.vikingArmy[s].strength)
        
        if self.saxonArmy[n].health <= 0:
            self.saxonArmy.pop(n)
        
        
    def saxonAttack(self):
        
        s= random.randint(0,len(self.saxonArmy)-1)
        n= random.randint(0,len(self.vikingArmy)-1)
        
        self.vikingArmy[n].receiveDamage(self.saxonArmy[s].strength)
        
        if self.vikingArmy[n].health <= 0:
            self.vikingArmy.pop(n)
                                                                          
    def showStatus(self):
        
        try:
            if type(self.vikingArmy[0]) == Viking and type(self.saxonArmy[0]) == Saxon:
            
                return 'Vikings and Saxons are still in the thick of battle.'
        
        except:
            try:
                if type (self.vikingArmy[0]) != Viking:

                    return 'Vikings have won the war of the century!'
                
                try:
                    if type (self.saxonArmy[0]) != Saxon:
                        
                        print('no')
                
                except:
                    
                    return 'Vikings have won the war of the century!'       
        
            except:    
                

                    return 'Saxons have fought for their lives and survive another day...'
