import random
from coups import coup_possible, jouer

# Écrire une fonction coup_aleatoire(g, j) qui joue un coup autorisé au hasard
# pour le joueur j.
# (Utiliser randint(a, b) du module random.)

def coup_aleatoire(g,j):
    while True:
        c = random.randint(0, 6)
        if coup_possible(g,c):
            jouer(g,j,c)
            break




