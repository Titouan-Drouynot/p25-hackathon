# INITIALISATION :

import config as c
import gestion_herbe as gh
import mouton as m
import Wolf as l
import pygame as pg

n = c.GRID_SIZE

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
    # for i in range (c.GRID_SIZE) :
    #   ligne = ""

    
    #verification des condition d'arret

    #statisiques : 
    
running = True


while running:

    clock.tick(5)

    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False

    grille = gh.update_grille(grille,proba_app = 0.1)

    #cycle moutons
    keys = list(dic_moutons.keys())
    for i in range(len(keys)):
        if keys[i] == -1:
            keys.pop(i)
        break
    for clef in keys:
        m.deplacement(dic_moutons[clef], grille)

        m.reproduction_mouton(grille, dic_moutons[clef], dic_moutons)

        gain = m.gain_energie_mouton(grille, dic_moutons[clef])
        dic_moutons[clef].energie += gain

    #cycle loups
    keys = list(dic_loups.keys())
    for i in range(len(keys)):
        if keys[i] == -1:
            keys.pop(i)
        break
    for clef in keys:
        l.deplacement(dic_loups[clef], grille)

        l.reproduction_loup(grille, dic_loups[clef], dic_loups)

        gain = l.gain_energie_loup(grille, dic_loups[clef])
        dic_loups[clef].energie += gain




    m.mort_mouton(dic_moutons, grille)
    l.mort_loup(dic_loups, grille)



    w,h = 20,20
    def damier():
        for i in range(n):
            for j in range(n):
                x,y = w*j , h*i
                rect = pg.Rect(x, y, w, h)
                if grille[i,j,0] == 0:
                    colour_case = (88,41,0)
                else:
                    colour_case = (0,255,0)
                pg.draw.rect(screen, colour_case, rect)

                rect = pg.Rect(x+10,y+10,w-10,w-10)
                
                if grille[i,j,1] != 0:
                    colour_case = (255,255,255)
                    pg.draw.rect(screen, colour_case, rect)
                
                if grille[i,j,2] !=0:
                    colour_case = (0,0,0)
                    pg.draw.rect(screen, colour_case, rect)

                
    
    damier()

    pg.display.update()

    print("Nombre de moutons vivants: ", len(dic_moutons) - 1)
    print("Nombre de moutons morts: ", dic_moutons[-1] - len(dic_moutons) + 1)
    print("Nombre de loups: ", len(dic_loups) - 1)
    print("Nombre de loups morts: ", dic_loups[-1] - len(dic_loups) + 1)