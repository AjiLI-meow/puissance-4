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
        c = input("Entrez le numéro de la colonne compris entre 1 et 7 : ")
        try:
            c = int(c)-1
        except ValueError:
            print("Saisissez un entier!")
            continue

        if c < 0 or c > 6:
            print("Saisissez un entier entre 1 et 7!")
            continue

        if coup_possible(g,c):
            jouer(g,j,c)
            break
        else:
            print("Ce coup n'est pas valide, choisissez à nouveau.")
