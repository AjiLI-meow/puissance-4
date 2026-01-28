from grille import grille_vide, affiche
from coups import coup_possible, jouer
from victoire import victoire, match_nul
from bot import coup_aleatoire

def main():
    g = grille_vide()
    j1=1;
    j2=2;

    while not victoire(g, j1) and not victoire(g, j2) and not victoire(g, j1):

        coup_aleatoire(g, j1)
        victoire(g, j1)
        affiche(g)


if __name__ == "__main__":
    main()