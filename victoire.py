# Écrire les fonctions suivantes, détectant un alignement de quatre pions du joueur j à partir de la case (l, c) :
# ○ horiz(g, j, l, c) : horizontal,
# ○ vert(g, j, l, c) : vertical,
# ○ diag_haut(g, j, l, c) : diagonale montante vers la droite,
# ○ diag_bas(g, j, l, c) : diagonale descendante vers la droite.

def horiz(g, j, l, c): # rather called right ??
    if c > 3:
        return False
    for k in range(4):
        if g[l][c + k] != j:
            return False
    return True

def vert(g, j, l, c):
    if l > 2:
        return False
    for k in range(4):
        if g[l+k][c] != j:
            return False
    return True

def diag_haut(g, j, l, c):
    if l > 2 or c > 3:
        return False
    for k in range(4):
        if g[l + k][c + k] != j:
            return False
    return True

def diag_bas(g, j, l, c):
    if l < 3 or c > 3:
        return False
    for k in range(4):
        if g[l - k][c + k] != j:
            return False
    return True

#Écrire une fonction victoire(g, j) qui indique si le joueur j a gagné.
def victoire(g, j):
    for l in range(6):
        for c in range(7):
            if g[l][c] == j:
                if (horiz(g, j, l, c) or
                    vert(g, j, l, c) or
                    diag_haut(g, j, l, c) or
                    diag_bas(g, j, l, c)):
                    return True
    return False





# Écrire une fonction match_nul(g) qui indique si la partie est nulle.
#Indication : il suffit d’examiner la ligne du haut.
def match_nul(g):
    return g[5].count(1) == g[5].count(2)
