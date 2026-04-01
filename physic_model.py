import numpy as np

def calcul_sigma_th(t, N, E, tau, eps_0, E_inf):
    # t est un tableau numpy contenant tous les temps
    somme = 0
    for i in range(N):
        somme += E[i] * np.exp(-t / tau[i])
    return eps_0 * (E_inf + somme)