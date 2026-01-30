# INITIALISATION :

import config as c
import gestion_herbe as gh
import moutons as m
import Wolf as l
import pygame as pg

# création grille taille n*n
grille = gh.initialisation_grille(c.GRID_SIZE)
# création du dictionnaire de moutons
dic_moutons = m.initialiser_moutons(grille)
# création du dictionnaire de loups
dic_loups = l.initialiser_loups(grille)

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()



# SIMULATION :

    #update_herbe(grille, GRASS_GROWTH_PROBABILITY)
    #update_moutons() 
    #update_loups()

    #vérification des morts (énergie < 1 ou age > limite)
    #reproduction
    #affichage
    '''for i in range (c.GRID_SIZE) :
        ligne = ""
        for j in range (c.GRID_SIZE) :
            if grille[i][j][1] > 0 :
                ligne += 'S'
            elif grille[i][j][2] > 0 :
                ligne += 'W'
            elif grille[i][j][0] :
                ligne += '#'
            else :
                ligne += '.'
        print(ligne)
    print("")'''
    
    #verification des condition d'arret

    #statisiques : 
    

running = True


while running:

    clock.tick(1)

    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False

    grille = gh.update_grille(grille,proba_app = 0.1)

    w,h = 20,20
    def damier():
        for i in range(n):
            for j in range(n):
                x,y = w*j , h*i
                rect = pg.Rect(x, y, w, h)
                if grille[i,j,0] == 0:
                    colour = (88,41,0)
                else:
                    colour = (0,255,0)
                pg.draw.rect(screen, colour, rect)
    
    damier()

    pg.display.update()

    print("Nombre de moutons vivants: " + len(dic_moutons))
    print("Nombre de moutons morts: " + m.NUMBER_SHEEP - len(dic_moutons))
    print("Nombre de loups: " + len(dic_loups))
    print("Nombre de moutons morts: " + m.NUMBER_WOLF - len(dic_loups))