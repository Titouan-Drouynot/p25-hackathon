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
    
def deplacement(loup, grille):
    x,y = loup.pos
    voisins = []
    if x > 0:
        voisins.append((x-1,y))
    if x < (c.GRID_SIZE - 1):
        voisins.append((x+1,y))
    if y > 0:
        voisins.append((x,y-1))
    if y < (c.GRID_SIZE - 1):
        voisins.append((x,y+1))
    valide = True
    for newpos in voisins :
        if grille[newpos[0], newpos[1], 1] > 0 :
            grille[newpos[0],newpos[1],2] = grille[x,y,2]
            grille[x,y,2] = 0
            loup.pos = newpos
            valide = False
            break
    while valide :
        new = rd.randint(0,len(voisins)-1)
        newpos = voisins[new]
        nx, ny = newpos
        if (grille[nx, ny, 1] == 0) and (grille[nx, ny, 2] == 0) :
            grille[newpos[0],newpos[1],2] = grille[x,y,2]
            grille[x,y,2] = 0 
            loup.pos = newpos
            valide = False
        else :
            voisins.pop(new)
        if len(voisins) == 0:
            valide = False
    

def initialiser_loups(grille):
    dic_loups = {-1 : c.INITIAL_WOLVES}
    nb_loups = min(c.INITIAL_WOLVES, max(c.GRID_SIZE**2-c.INITIAL_SHEEP,0))
    nb_loups_places = 0

    while nb_loups != 0:
        i = rd.randint(0,c.GRID_SIZE-1)
        j = rd.randint(0,c.GRID_SIZE-1)

        if (grille[i,j,1] == 0) and (grille[i,j,2] == 0):
            nb_loups -= 1
            nb_loups_places += 1
            dic_loups[nb_loups_places] = Loup(i,j, c.WOLF_INITIAL_ENERGY, 0)
            grille[i,j,2] = nb_loups_places
    return dic_loups


def gain_energie_loup(grille, loup):
    x, y = loup.pos
    if grille[x][y][1] != 0:
        return c.WOLF_ENERGY_FROM_SHEEP -c.WOLF_ENERGY_LOSS_PER_TURN
    return -c.WOLF_ENERGY_LOSS_PER_TURN
    
    



def reproduction_loup(grille, loup, dic_loups):
    if loup.energie > c.WOLF_REPRODUCTION_THRESHOLD:
        x, y = loup.pos
        voisins = [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]
        for i in range(len(voisins)-1, -1, -1):
            if (voisins[i][0] < 0)or(voisins[i][0] > c.GRID_SIZE-1)or(voisins[i][1] < 0)or(voisins[i][1] > c.GRID_SIZE-1):
                voisins.pop(i)
        valide = False
        while not valide :
            new = rd.randint(0,len(voisins)-1)
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
            dic_loups[-1] += 1
            nouveau_loup = Loup(nx, ny, c.WOLF_INITIAL_ENERGY, 0)
            loup.energie = loup.energie - c.REPRODUCTION_ENERGY_COST
            dic_loups[dic_loups[-1]] = nouveau_loup
            grille[nx,ny,2] = dic_loups[-1]

def mort_loup(dico_loups, grille):
    keys = list(dico_loups.keys())
    for i in range(len(keys)):
        if keys[i] == -1:
            keys.pop(i)
            break
    for key in keys:
        loup = dico_loups[key]
        x,y = loup.pos
        if (loup.age > c.WOLF_MAX_AGE) or (loup.energie < 0):
            del dico_loups[key]
            grille[x,y,2] = 0