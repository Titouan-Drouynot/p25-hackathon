import pygame as pg
import gestion_herbe as gh

n = 30
grille = gh.initialisation_grille(n)

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

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