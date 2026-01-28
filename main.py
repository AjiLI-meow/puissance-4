from grille import grille_vide, affiche
from coups import coup_possible, jouer
from victoire import victoire, match_nul
from players import coup_aleatoire, coup_humain
import sys


def main():
    while True:
        g = grille_vide()
        j1=1; #X
        j2=2; #O

        # chose mode bot or huamin
        while True:
            mode = input("Entrez 'b' pour regarder deux bots jouer, entrez 'h' pour jouer : ").lower()
            if mode in ["b","h"]:
                break
            else:
                print('Permission refused')

        # game play loop
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

        # play again ?
        while True:
            replay=input("Rejouer ? Entrez o ou n (oui ou non) : ").lower()
            if replay not in ['o', 'n']:
                print("Saisissez 'o' ou 'n' !")
                continue
            if replay == 'o':
                break
            else:
                print('Bye !')
                sys.exit()

if __name__ == "__main__":
    main()