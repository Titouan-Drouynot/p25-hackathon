import numpy as np
import random 

" génère une grille de taille N x N qui modélise le plateau de jeu"



def initialisation_grille(n,taux = 0.3):

    grille = np.zeros((n,n,3),dtype = int)
    # initialement de l'herbe partout

    nb_herbe = np.floor(taux * n**2)

    while nb_herbe != 0:
        i = random.randint(0,n-1)
        j = random.randint(0,n-1)

        if not(grille[i,j,0]):
            grille[i,j,0] = 1
            nb_herbe -= 1
    
    return(grille)

grille_i = initialisation_grille(10)

def update_grille(grille,proba_app = 0.1):

    n = len(grille)

    # génération spontanée d'herbe
    for i in range(n):
        for j in range (n):

            if not(grille[i,j,0]):

                grille[i,j,0] = np.random.binomial(1,proba_app)
    
    return grille


