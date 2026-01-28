from grille import grille_vide, affiche
from coups import coup_possible, jouer
from victoire import victoire, match_nul
from bot import coup_aleatoire

def main():
    g = grille_vide()
    j1=1;
    j2=2;

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
            coup_aleatoire(g,j1)
            affiche(g)
            coup_aleatoire(g, j2)
            affiche(g)



if __name__ == "__main__":
    main()