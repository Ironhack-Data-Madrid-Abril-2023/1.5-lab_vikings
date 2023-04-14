
# Soldier


class Soldier:
    
    def __init__(self, health, strength) -> None:
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength) -> None:
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return super().attack()


# Saxon


class Saxon:
    pass

# War


class War:
    pass
