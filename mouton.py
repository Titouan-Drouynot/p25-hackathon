import random as rd
import config as c
import numpy as np

class Mouton:
    def __init__(self, x, y, energie, age):
        self.pos = (x,y)
        self.energie = energie
        self.age = age

    def update_energie(self, gain):
        self.energie += gain
    
    def update_age(self):
        self.age += 1


def deplacement(mouton, grille):
    x,y = mouton.pos
    voisins = [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]
    for p in voisins :
        if (0 <= p[0] < c.GRID_SIZE) and (0 <= p[1] < c.GRID_SIZE) :
            if grille[p[0], p[1], 0] == 1 :
                x,y = p
                #self.alimentation()
        else :
            valide = False
            while not valide :
                new = rd.randint(0,3)
                newpos = voisins[new]
                nx, ny = newpos
                if (grille[nx, ny, 1] == 0) and (grille[nx, ny, 2] == 0) :
                    loup.pos = newpos
                    valide = True
                else :
                    voisins.pop(new)
                if len(voisins) == 0:
                    valide = True

NUMBER_SHEEP = c.INITIAL_SHEEP

def initialiser_moutons(grille):
    dic_moutons = {}

    nb_mouton = np.max(c.INITIAL_SHEEP, c.GRID_SIZE**2)
    nb_moutons_places = 0

    while nb_mouton != 0:
        i = rd.randint(0,c.GRID_SIZE-1)
        j = rd.randint(0,c.GRID_SIZE-1)

        if grille[i,j,1] == 0:
            nb_mouton -= 1
            nb_moutons_place += 1
            dic_moutons[nb_moutons_places] = Mouton(i,j, c.SHEEP_INITIAL_ENERGY, 0)
            grille[i,j,1] = nb_moutons_places
    return dic_moutons



def gain_energie_mouton(grille, mouton):
    x, y = mouton.pos
    if grille[x][y][0] == 1:
        gain = c.SHEEP_ENERGY_FROM_GRASS
    return gain - c.SHEEP_ENERGY_LOSS_PER_TURN


def reproduction_mouton(grille, mouton, dic_moutons):
    if mouton.energie > c.SHEEP_REPRODUCTION_THRESHOLD:
        NUMBER_SHEEP += 1
        x, y = mouton.x, mouton.y
        voisins = [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]
        for i in range(len(voisins)):
            if (voisins[i, 0] < 0)or(voisins[i, 0] > c.GRID_SIZE-1)or(voisins[i, 1] < 0)or(voisins[i, 1] > c.GRID_SIZE-1):
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
            nouveau_mouton = Mouton(nx, ny, c.SHEEP_INITIAL_ENERGY, 0)
            mouton.energie = mouton.energie - c.REPRODUCTION_ENERGY_COST
            dic_moutons[NUMBER_SHEEP] = nouveau_mouton

def mort_mouton(dico_moutons, grille):
    for key in dico_moutons:
        mouton = dico_moutons[key]
        x,y = mouton.pos
        if (mouton.age > c.SHEEP_MAX_AGE) or (mouton.energy < 0) or (grille[x,y,2] != 0):
            del dico_moutons[key]
            grille[x,y,1] = 0
    
