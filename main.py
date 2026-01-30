# INITIALISATION :

import config as c
import gestion_herbe as herbe

# création grille taille n*n
grille = herbe.initialisation_grille(c.GRID_SIZE)
# création du dictionnaire de moutons
#initialisation_moutons(grille, INITIAL_SHEEP)
# création du dictionnaire de loups
#initialisation_loups(grille, INITIAL_WOLVES)



# SIMULATION :

for i in range (c.MAX_TURNS):

    #update_herbe(grille, GRASS_GROWTH_PROBABILITY)
    #update_moutons() 
    #update_loups()

    #vérification des morts (énergie < 1 ou age > limite)
    #reproduction
    #affichage
    for i in range (c.GRID_SIZE) :
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
    print("")
    

    #verification des condition d'arret
