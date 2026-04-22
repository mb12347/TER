import numpy as np
import matplotlib.pyplot as plt

from data_loader import read_relaxation
from physic_model import calcul_sigma_th
from solver import descente_gradient



# On récupère les donnees experimentales avec la fonction
# Dans main.py, ligne 11
t, sigma_exp = read_relaxation("donnees_relaxation_4.TXT", S0=44.0376)
# On initialise les parametres de depart
eps_0 = 0.05
N_ressorts = 4
E_inf_depart  = 10.0          
E_depart  = [5.0, 3.0, 1.5, 0.5] 
tau_depart = [1.0, 10.0, 50.0, 200.0] 
alpha_choisi  = 0.01    

# On lance la descente de gradient
E_inf_opt, E_opt, tau_opt, erreurs = descente_gradient(
    sigma_exp, t, N_ressorts, eps_0, 
    E_inf_depart, E_depart, tau_depart, 
    alpha_choisi
)

print("Parametres trouves :", E_inf_opt, E_opt, tau_opt)

# On calcule la courbe theorique finale pour l'affichage 
sigma_theorique_final = calcul_sigma_th(t, N_ressorts, E_opt, tau_opt, eps_0, E_inf_opt)

# 5. Afficher le graphique
plt.plot(t, sigma_exp, label="Donnees experimentales", color="blue")
plt.plot(t, sigma_theorique_final, label="Modele optimise", color="red", linestyle="--")
plt.legend()
plt.show()


# Vérifier calcul du gradient
# Validation avec fonction connue et gradient connu