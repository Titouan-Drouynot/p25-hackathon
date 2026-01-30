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
            if (0 <= p[0] < n-1) and (0 <= p[1] < n) :
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











