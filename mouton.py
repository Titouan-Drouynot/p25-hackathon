import random as rd

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
        x, y = mouton.x, mouton.y
        voisins = [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]
        for i in range(len(voisins)):
            if (voisins[i, 0] < 0)or(voisins[i, 0] > GRID_SIZE-1)or(voisins[i, 1] < 0)or(voisins[i, 1] > GRID_SIZE-1):
                voisins.pop(i)
        valide = False
        while not valide :
            new = rd.randint(0,len(voisins))
            newpos = voisins[new]
            nx, ny = newpos
            if (grille[nx, ny, 2] == 0) and (grille[nx, ny, 1] == 0) :
                valide = True
            else :
                voisins.pop(new)
            if len(voisins) == 0:
                valide = True
                nx = -1
        if nx != -1:
            nouveau_mouton = Mouton(nx, ny, SHEEP_INITIAL_ENERGY, 0)
            dic_moutons[NUMBER_SHEEP] = nouveau_mouton

"""def mort_mouton(mouton):
    if mouton.age > SHEEP_MAX_AGE :"""
