import random as rd

# Énergie
SHEEP_INITIAL_ENERGY = 20
WOLF_INITIAL_ENERGY = 40
SHEEP_ENERGY_FROM_GRASS = 15
WOLF_ENERGY_FROM_SHEEP = 35
SHEEP_ENERGY_LOSS_PER_TURN = 1
WOLF_ENERGY_LOSS_PER_TURN = 2  # Les loups perdent plus d'énergie

# Reproduction
SHEEP_REPRODUCTION_THRESHOLD = 50
WOLF_REPRODUCTION_THRESHOLD = 80
REPRODUCTION_ENERGY_COST = 20

# Âge
SHEEP_MAX_AGE = 50  # Tours avant mort naturelle
WOLF_MAX_AGE = 40


class Loup :

    def __init__(self, x, y, energie, age):
        self.pos = (x,y)
        self.energie = energie
        self.age = age
    
    def deplacement(self, grille, n):
        x,y = self.pos
        voisins = [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]
        for p in voisins :
            if (0 <= p[0] < GRID_SIZE) and (0 <= p[1] < GRID_SIZE) :
                if grille[p[0], p[1], 1] == 1 :
                    x,y = p
                    self.alimentation()
                else :
                    valide = False
                    while not valide :
                        new = rd.randint(0,3)
                        newpos = voisins[new]
                        nx, ny = newpos
                        if grille[nx, ny, 2] == 0 :
                            self.pos = new
                            valide = True
                        else :
                            voisins.pop(new)
                        if len(voisins) == 0:
                            valide = True
    
    def alimentation(self):
        self.energie = self.energie + WOLF_ENERGY_FROM_SHEEP


def gain_energie_loup(grille, loup):
    x, y = loup.pos
    if grille[x][y][1] != 0:
        gain = WOLF_ENERGY_FROM_SHEEP
    else :
        gain = -WOLF_ENERGY_LOSS_PER_TURN
    return gain

NUMBER_WOLF = INITIAL_WOLF

def reproduction_loup(grille, loup, dic_loups):
    if loup.energie > SHEEP_REPRODUCTION_THRESHOLD:
        NUMBER_WOLF += 1
        x, y = loup.x, loup.y
        voisins = [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]
        for i in range(len(voisins)):
            if (voisins[i, 0] < 0)or(voisins[i, 0] > GRID_SIZE-1)or(voisins[i, 1] < 0)or(voisins[i, 1] > GRID_SIZE-1):
                voisins.pop(i)
        valide = False
        while not valide :
            new = rd.randint(0,3)
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
            nouveau_loup = Loup(nx, ny, WOLF_INITIAL_ENERGY, 0)
            dic_loups[NUMBER_WOLF] = nouveau_loup
