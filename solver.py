import numpy as np

from physic_model import calcul_sigma_th
from maths import S, grad_S

def descente_gradient(sigma_exp, t, N, eps_0, E_inf_init, E_init, tau_init, alpha):
    
    return E_inf, E, tau, historique_erreur