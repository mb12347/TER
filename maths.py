import numpy as np

def S(sigma_exp, sigma_th_vals):
    return np.sum((sigma_exp - sigma_th_vals)**2)

def grad_S(E_inf, E, tau, sigma_exp, sigma_th_vals, N, eps_0, t):
    # Création du vecteur gradient
    grad = []
    
    # On calcule l'écart une seule fois
    diff = sigma_exp - sigma_th_vals 

    # Calcul de dS/dEinf
    dS_dEinf = -2 * eps_0 * np.sum(diff)

    # Calcul des dS/dEi
    grad_E = []
    for i in range(N):
        dS_dEi = -2 * eps_0 * np.sum(diff * np.exp(-t / tau[i]))
        grad_E.append(dS_dEi)

    # Calcul des dS/dtaui
    grad_tau = []
    for i in range(N):
        dS_dtaui = -2 * eps_0 * np.sum(diff * E[i] * (t / tau[i]**2) * np.exp(-t / tau[i]))
        grad_tau.append(dS_dtaui)
    
    # On renvoie le gradient
    return dS_dEinf, grad_E, grad_tau