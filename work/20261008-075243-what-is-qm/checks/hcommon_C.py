# shared helpers for candidate C checks
import numpy as np
from scipy import constants as k
R_inf = k.physical_constants['Rydberg constant'][0]  # 1/m
m_e, m_p = k.m_e, k.m_p
m_d = k.physical_constants['deuteron mass'][0]
def R_M(M): return R_inf/(1+m_e/M)
def vac_nm(n_hi, n_lo, M=m_p):
    return 1e9/(R_M(M)*(1/n_lo**2-1/n_hi**2))
def air_nm(lam_vac_nm):
    s2 = (1e3/lam_vac_nm)**2  # (1/um)^2, Ciddor 1996 dispersion
    n = 1 + 0.05792105/(238.0185-s2) + 0.00167917/(57.362-s2)
    return lam_vac_nm/n
