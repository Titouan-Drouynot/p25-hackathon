import random as rd

class animal :

    def __init__(self, x, y, energie, age, mouton):
        self.pos = (x,y)
        self.energie = energie
        self.age = age
        self.mouton = mouton
    
    def deplacement (self, n):
        x,y = self.pos
        voisins = [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]
        
        new = rd.randint(0,3) :




def gain_energie_loup(grille, loup):
    x, y = loup.pos
    if grille[x][y][1] != 0:
        gain = WOLF_ENERGY_FROM_SHEEP
    else :
        gain = -WOLF_ENERGY_LOSS_PER_TURN
    return gain



