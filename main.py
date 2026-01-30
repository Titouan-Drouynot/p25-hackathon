# Configuration
GRID_SIZE = 30
INITIAL_SHEEP = 50
INITIAL_WOLVES = 10
INITIAL_GRASS_COVERAGE = 0.3

SHEEP_INITIAL_ENERGY = 20
WOLF_INITIAL_ENERGY = 40
SHEEP_ENERGY_FROM_GRASS = 15
WOLF_ENERGY_FROM_SHEEP = 35
SHEEP_ENERGY_LOSS_PER_TURN = 1
WOLF_ENERGY_LOSS_PER_TURN = 2

SHEEP_REPRODUCTION_THRESHOLD = 50
WOLF_REPRODUCTION_THRESHOLD = 80
REPRODUCTION_ENERGY_COST = 20

SHEEP_MAX_AGE = 50
WOLF_MAX_AGE = 40

GRASS_GROWTH_PROBABILITY = 0.08

MAX_TURNS = 500



# INITIALISATION :

# création grille taille n*n
# création de la liste des moutons
# création de la liste des loups



# SIMULATION :

#incrémenter age
#update herbe
#phase moutons : déplacement, alimentation, perte energie 
#phase loups : déplacement, chasse, perte energie
#vérification des morts (énergie < 1 ou age > limite)
#reproduction
#affichage
#verification des condition d'arret
