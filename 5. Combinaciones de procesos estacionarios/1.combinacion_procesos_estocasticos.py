import numpy as np

# Generar un proceso estacionario zt con 1000 observaciones
np.random.seed(42)
zt = np.random.normal(0, 1, 1000)

# Calcular el proceso wt como la diferencia entre zt y z(t-1)
wt = np.diff(zt)

# Calcular la esperanza de wt
esperanza_wt = np.mean(wt)
print("Esperanza de wt:", esperanza_wt)

# Calcular la varianza de wt
var_wt = np.var(wt)
print("Varianza de wt:", var_wt)

# Calcular la función de autocovarianza de wt
def autocov(wt, k):
    wt_t = wt[:-k]
    wt_t_plus_k = wt[k:]
    return np.mean((wt_t - np.mean(wt_t)) * (wt_t_plus_k - np.mean(wt_t_plus_k)))

k = 5
autocov_wt = autocov(wt, k)
print(f"Autocovarianza de wt con retardo {k}:", autocov_wt)
