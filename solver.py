import numpy as np

from physic_model import calcul_sigma_th
from maths import S, grad_S

def descente_gradient(sigma_exp, t, N, eps_0, E_inf_init, E_init, tau_init, alpha):
    
    """
    Entrées:

    sigma_exp    : contrainte expérimentale
    t            : vecteur temps
    N_ressorts   : nombre d'éléments de Maxwell
    eps_0        : déformation imposée
    E_inf_depart : valeur initiale de E_inf
    E_depart     : valeurs initiales des E_i
    tau_depart   : valeurs initiales des tau_i
    alpha        : pas de gradient (learning rate)

    Sorties :

    E_inf 
    E 
    tau 
    """
    niter = 5000 

    #Initialisation des paramètres d'entrées 

    E_inf = E_inf_init
    E     = E_init
    tau   = tau_init
    erreur = []

    iter = 0 
    for iteration in range(niter) :

        #calcul du coût de cette itération 
        sigma_th = calcul_sigma_th(t, N, E, tau, eps_0, E_inf)
        cout = S(sigma_exp,sigma_th)
        erreur.append(cout)

        #calcul du gradient E_int E tau
        grad_E_inf, grad_E, grad_tau = grad_S(E_inf, E, tau, sigma_exp, sigma_th, N, eps_0, t)

        #mise à jour de E_inf, E, tau (theta = theta - alpha * grad)
        #E_inf est un scalaire
        E_inf = E_inf - alpha * grad_E_inf
        #E et tau sont des listes 
        E = [E[i] - alpha * grad_E[i] for i in range(N)]
        tau = [tau[i] - alpha * grad_tau[i] for i in range(N)]
        iter = iter + 1

    print("nb iter:  " , iter)
    print("erreur à la dernier iter :  ", erreur[-1])

    return E_inf, E, tau, erreur