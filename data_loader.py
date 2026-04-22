import numpy as np

import numpy as np

def read_relaxation(nom_fichier, S0=44.0376):
    donnees = np.genfromtxt(nom_fichier, delimiter=';', skip_header=25)
    t_complet = donnees[:, 0]
    sigma_complet = (donnees[:, 3] * 1000) / S0

    # On ne garde que la phase de relaxation (après le pic à ~46s)
    temps_debut_relaxation = 46.0
    temps_max = 400.0
    masque = (t_complet >= temps_debut_relaxation) & (t_complet <= temps_max)

    t_relax = t_complet[masque]
    sigma_relax = sigma_complet[masque]

    # On sous-échantillonne (1 point sur 10 suffit)
    t_final = t_relax[::10] - t_relax[0]   # ← remise à zéro du temps
    sigma_final = sigma_relax[::10]

    return t_final, sigma_final

#faire pour les deux courbes en meme temps