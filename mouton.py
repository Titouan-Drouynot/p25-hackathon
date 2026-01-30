class mouton:
    def __init__(self, x, y, energie, age, mouton):
        self.pos = (x,y)
        self.energie = energie
        self.age = age

    def update_energie(self, gain):
        self.energie += gain
    
    def update_age(self):
        self.age += 1



def gain_energie_mouton(grille, mouton):
    x, y = mouton.pos
    if grille[x][y][0] == 1:
        gain = SHEEP_ENERGY_FROM_GRASS
    else :
        gain = -SHEEP_ENERGY_LOSS_PER_TURN
    return gain

def gain_energie_loup(grille, loup):
    x, y = loup.pos
    if grille[x][y][1] != 0:
        gain = WOLF_ENERGY_FROM_SHEEP
    else :
        gain = -WOLF_ENERGY_LOSS_PER_TURN
    return gain
