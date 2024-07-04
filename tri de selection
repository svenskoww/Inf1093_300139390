def tri_selection_taille(fichiers):
    for i in range(len(fichiers)):
        min_index = i
        for j in range(i+1, len(fichiers)):
            if fichiers[j][2] < fichiers[min_index][2]:
                min_index = j
        fichiers[i], fichiers[min_index] = fichiers[min_index], fichiers[i]
    return fichiers
