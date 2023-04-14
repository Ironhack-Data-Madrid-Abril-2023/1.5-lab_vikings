
# Soldier


# class Soldier:

#     def init(self, health, strength):
#         self.health=health
#         self.strength=strength

#     def attack(self):
#         return self.strength

#     def receiveDamage(self, damage):
#         self.health-=damage

class Soldier:
    
    def __init__(self, health, strength) -> None:
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health -= damage

# Viking


class Viking:
    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass
