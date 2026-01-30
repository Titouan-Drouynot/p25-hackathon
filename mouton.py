class Mouton:
    def __init__(self, x, y, energie, age):
        self.pos = (x,y)
        self.energie = energie
        self.age = age

    def update_energie(self, gain):
        self.energie += gain
    
    def update_age(self):
        self.age += 1

NUMBER_SHEEP = INITIAL_SHEEP

def gain_energie_mouton(grille, mouton):
    x, y = mouton.pos
    if grille[x][y][0] == 1:
        gain = SHEEP_ENERGY_FROM_GRASS
    return gain - SHEEP_ENERGY_LOSS_PER_TURN


def reproduction_mouton(grille, mouton, dic_moutons):
    if mouton.energie > SHEEP_REPRODUCTION_THRESHOLD:
        NUMBER_SHEEP += 1
        nouveau_mouton = Mouton(mouton.x, mouton.y, SHEEP_INITIAL_ENERGY, 0)
        dic_moutons[NUMBER_SHEEP] = nouveau_mouton
