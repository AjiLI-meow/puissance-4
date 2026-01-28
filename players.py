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


def coup_humain(g,j):

    while True:
        c = input("Choisissez un coup valid : ")
        c = int(c)
        if coup_possible(g,c):
            jouer(g,j,c)
            break
        else:
            print("Ce coup n'est pas valide, choisissez à nouveau.")
