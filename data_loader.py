import numpy as np

def read_relaxation(nom_fichier, S0=44.0376):

    # on lit le fichier
    donnees = np.genfromtxt(nom_fichier, delimiter=';', skip_header=25)
    t_complet = donnees[:, 0]
    sigma_complet = (donnees[:, 3] * 1000) / S0
    
    # on coupe la fin à partir de 400 s on s'en fiche
    temps_max = 400.0
    masque_utile = (t_complet <= temps_max)
    
    t_utile = t_complet[masque_utile]
    sigma_utile = sigma_complet[masque_utile]
    
    # avant 46s on fait un grand pas de temps et après on "raffine"
    temps_limite = 46.0
    masque_debut = (t_utile < temps_limite)
    masque_fin = (t_utile >= temps_limite)
    
    # on prend 1 point sur 200
    t_debut = t_utile[masque_debut][::200]
    sigma_debut = sigma_utile[masque_debut][::200]
    
    # on prend 1 point sur 10
    t_fin = t_utile[masque_fin][::10]
    sigma_fin = sigma_utile[masque_fin][::10]
    
    t_final = np.concatenate((t_debut, t_fin))
    sigma_final = np.concatenate((sigma_debut, sigma_fin))
    
    return t_final, sigma_final

#faire pour les deux courbes en meme temps
