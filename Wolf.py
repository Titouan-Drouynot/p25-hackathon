import random as rd
import config as c


class Loup :

    def __init__(self, x, y, energie, age):
        self.pos = (x,y)
        self.energie = energie
        self.age = age
    
    def deplacement(self, grille, n):
        x,y = self.pos
        voisins = [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]
        for p in voisins :
            if (0 <= p[0] < n) and (0 <= p[1] < n) :
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

    






    def gain_energie_loup(grille, loup):
        x, y = loup.pos
        if grille[x][y][1] != 0:
            gain = c.WOLF_ENERGY_FROM_SHEEP
        else :
            gain = -c.WOLF_ENERGY_LOSS_PER_TURN
        return gain
    
    






