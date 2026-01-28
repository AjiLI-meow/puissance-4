from grille import grille_vide, affiche
from coups import coup_possible, jouer
from victoire import victoire, match_nul
from players import coup_aleatoire, coup_humain


def main():
    g = grille_vide()
    j1=1; #X
    j2=2; #O


    while True:
        mode = input("Entrez 'b' pour regarder deux bots jouer, entrez 'h' pour jouer : ")
        if mode in ["b","h"]:
            break
        else:
            print('Permission refused')

    while True:
        if match_nul(g):
            print("Match nul!")
            break

        if victoire(g,j1):
            print("Joueur 1 gagne!")
            break
        elif victoire(g,j2):
            print("Joueur 2 gagne!")
            break
        else:
            if mode == "b":
                coup_aleatoire(g,j1)
            elif mode == "h":
                coup_humain(g,j1)
            affiche(g)
            coup_aleatoire(g, j2)
            affiche(g)



if __name__ == "__main__":
    main()