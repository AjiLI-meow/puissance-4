# Écrire une fonction coup_possible(g, c) qui indique si un coup peut être joué dans la colonne c.
def coup_possible(g,c):
    if c<0 or c>6:
        return False
    else:
        return g[5][c] != 0


# Écrire une fonction jouer(g, j, c) qui place un pion du joueur j dans la colonne c (supposée non pleine).
# La fonction modifie directement la grille g.
def jouer(g,j,c):
    #if coup_possible(g,c): verif dans main
        for l in range(6):
            if g[l][c] == 0:
                g[l][c] = j
                break