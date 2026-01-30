import random as rd
import config as c


class Loup :

    def __init__(self, x, y, energie, age):
        self.pos = (x,y)
        self.energie = energie
        self.age = age

    def update_energie(self, gain):
        self.energie += gain
    
    def update_age(self):
        self.age += 1
    
    def deplacement(self, grille, n):
        x,y = self.pos
        voisins = [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]
        for p in voisins :
            if (0 <= p[0] < c.GRID_SIZE) and (0 <= p[1] < c.GRID_SIZE) :
                if grille[p[0], p[1], 1] == 1 :
                    x,y = p
                    #self.alimentation()
            else :
                valide = False
                while not valide :
                    new = rd.randint(0,3)
                    newpos = voisins[new]
                    nx, ny = newpos
                    if grille[nx, ny, 2] == 0 :
                        self.pos = newpos
                        valide = True
                    else :
                        voisins.pop(new)
                    if len(voisins) == 0:
                        valide = True
    
    #def alimentation(self):
    #    self.energie = self.energie + WOLF_ENERGY_FROM_SHEEP


def initialiser_loups(grille):
    dic_loups = {}
    nb_loups = np.max(c.INITIAL_WOLVES, c.GRID_SIZE**2-c.INITIAL_SHEEP)
    nb_loups_places = 0

    while nb_loups != 0:
        i = rd.randint(0,c.GRID_SIZE-1)
        j = rd.randint(0,c.GRID_SIZE-1)

        if (grille[i,j,1] == 0) and (grille[i,j,2] == 0):
            nb_loups -= 1
            nb_loups_place += 1
            dic_loups[nb_loups_places] = Loup(i,j, c.WOLF_INITIAL_ENERGY, 0)
            grille[i,j,2] = nb_loups_places
    return dic_loups


def gain_energie_loup(grille, loup):
    x, y = loup.pos
    if grille[x][y][1] != 0:
        gain = c.WOLF_ENERGY_FROM_SHEEP 
    return gain -c.WOLF_ENERGY_LOSS_PER_TURN
    
    

NUMBER_WOLF = c.INITIAL_WOLVES

def reproduction_loup(grille, loup, dic_loups):
    if loup.energie > c.WOLF_REPRODUCTION_THRESHOLD:
        NUMBER_WOLF += 1
        x, y = loup.x, loup.y
        voisins = [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]
        for i in range(len(voisins)):
            if (voisins[i, 0] < 0)or(voisins[i, 0] > c.GRID_SIZE-1)or(voisins[i, 1] < 0)or(voisins[i, 1] > c.GRID_SIZE-1):
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
            nouveau_loup = Loup(nx, ny, c.WOLF_INITIAL_ENERGY, 0)
            loup.energie = loup.energie - c.REPRODUCTION_ENERGY_COST
            dic_loups[NUMBER_WOLF] = nouveau_loup

def mort_loup(dico_loups, grille):
    for key in dico_loups:
        loup = dico_loups[key]
        x,y = loup.pos
        if (loup.age > c.WOLF_MAX_AGE) or (loup.energy < 0):
            del dico_loups[key]
            grille[x,y,2] = 0