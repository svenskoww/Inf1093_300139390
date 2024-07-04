def tri_bulles_nom(fichiers):
    n = len(fichiers)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if fichiers[j][0] > fichiers[j+1][0]:
                fichiers[j], fichiers[j+1] = fichiers[j+1], fichiers[j]
    return fichiers
