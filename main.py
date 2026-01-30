# INITIALISATION :

# création grille taille n*n
grille = initialisation_grille(GRID_SIZE)
# création du dictionnaire de moutons
initialisation_moutons(grille, INITIAL_SHEEP)
# création du dictionnaire de loups
initialisation_loups(grille, INITIAL_WOLVES)



# SIMULATION :

for i in range (MAX_TURNS):
    #update herbe
    update_herbe(grille, GRASS_GROWTH_PROBABILITY)
    #phase moutons : déplacement, alimentation, perte energie
    update_moutons() 
    #phase loups : déplacement, chasse, perte energie
    update_loups()
    #vérification des morts (énergie < 1 ou age > limite)
    #reproduction
    #affichage
    #verification des condition d'arret
