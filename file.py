import vikingsClasses as vk
import random

""" Las clases VikingArmy y SaxonArmy, serán las encargadas de crear los ejércitos
Seguirán las siguientes pautas:

    + name (sólo para Vikings): se cogerá un nombre aleatorio de una lista de 100 
                                nombres vikingos (se pueden repetir)

    + health:   nº aleatorio entre 80-100 para vikingos 
                nº aleatorio entre 90-110 para saxons

    + strength  nº aleatorio entre 60-80 para vikingos
                nº aleatorio entre 50-70 para saxons
    

La clase InitWar recibirá como parámetros el número de soldados de cada ejercito
sera la encargada de:

    + Asignar los soldados para la guerra

    + Invocar a la clase War del módulo vikingClasses
                
    """

class VikingArmy:
    VIK_NAMES = ['Ragnar', 'Ivar', 'Bjorn', 'Harald', 'Erik', 'Leif', 'Sigurd',
                'Olaf', 'Thorstein', 'Hakon', 'Gunnar', 'Asgeir', 'Sten', 
                'Knut', 'Sven', 'Erling', 'Magnus', 'Finn', 'Vidar', 
                'Hans', 'Orvar', 'Gudmund', 'Bard', 'Eirik', 'Gudbrand', 
                'Ole', 'Birger', 'Tore', 'Arne', 'Halvor', 'Trygve', 'Gjermund',
                'Jens', 'Rolf', 'Lars', 'Odd', 'Sindre', 'Peder', 'Vegard',
                'Herman', 'Johannes', 'Einar', 'Nils', 'Per', 'Geir', 'Karl', 
                'Dag', 'Ludvig', 'Ola', 'Kjell', 'Stian', 'Inge', 'Anders', 
                'Øyvind', 'Morten', 'Joakim', 'Kåre', 'Pål', 'Håkon', 'Åge', 
                'Knut', 'Jan', 'Even', 'Terje', 'Erlend', 'Lasse', 'Tommy', 
                'Børre', 'Arvid', 'Jon', 'Espen', 'Fredrik', 'Marius', 'Simen', 
                'Sondre', 'Christian', 'Erik', 'Hans', 'Kai', 'Kristian', 
                'Steffen', 'Svein', 'Torbjørn', 'Trond', 'Vidar', 'Wilhelm', 
                'Yngve', 'Øivind', 'Bjarte', 'David', 'Eivind', 'Gard', 'Ivar', 
                'Jørgen', 'Kevin', 'Magnar', 'Ole', 'Petter']
    
    def __init__(self, n_vikings) -> None:
        self.n_vikings = n_vikings
        self.army = []

    def create_army(self) -> list:
        global VIK_NAMES
        name = ''
        for _ in range(len(self.n_vikings)):
            name = random.choice(VIK_NAMES)
            self.army.append(vk.Viking(name= name, 
                                       health=random.randint(80,100),
                                       strength=random.randint(60,80)))
        return self.army


class SaxonArmy:
    
    def __init__(self, n_saxons) -> None:
        self.n_saxons = n_saxons
        self.army = []

    def create_army(self) -> list:
        for _ in range(len(self.n_saxons)):
            self.army.append(vk.Saxon(health=random.randint(80,100),
                                      strength=random.randint(60,80)))
        return self.army
            

class InitWar():
    
    def __init__(self,n_vikings,n_saxons) -> None:
        self.n_vikings = n_vikings
        self.n_saxons = n_saxons

    def assign_army(self):
        sax = SaxonArmy(self.n_saxons)
        vik = VikingArmy(self.n_vikings)
        sax_army = sax.create_army()
        vik_army = vik.create_army()

        for viking in vik_army:
            vk.War.addViking(viking=viking)
        for saxon in sax_army:
            vk.War.addSaxon(saxon=saxon)


        
                        

          

