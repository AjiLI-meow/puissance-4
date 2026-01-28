from time import sleep

def grille_vide():
    return [[0 for c in range(7)] for l in range(6)]

def affiche(g):
    for l in range(5,-1,-1):
        for c in range(7):
            if g[l][c] == 1:
                print("X", end=' ')
            elif g[l][c] == 2:
                print("O", end=' ')
            elif g[l][c] == 0:
                print("*", end=' ')
        print("")
    print("1 2 3 4 5 6 7")
    sleep(1)
