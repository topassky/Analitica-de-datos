from nivel_serie import Nivel_serie
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#plt.style.use('_mpl-gallery')

# make data
df = pd.read_table("parados.dat", sep="\s+", header=None)

# Se segmenta el numero de la variable parados.
tiempo = np.linspace(1, len(df[2])+1, len(df[2]))
parados = df[2]

nivel_serie = Nivel_serie(tiempo, parados)
tendencia =nivel_serie.calculo()

#--------------------------------------------------
E_t = parados - tendencia 

nivel_serie_Et = Nivel_serie(tiempo, E_t)
tendencia_Et = nivel_serie_Et.calculo()


# Grafica de la series original.
fig, ax = plt.subplots()
ax.plot(tiempo, parados, linewidth=2.0)
ax.plot(tiempo, tendencia, linewidth=2.0)
ax.plot(tiempo, E_t, linewidth=2.0)
ax.plot(tiempo, tendencia_Et, linewidth=2.0)
plt.show()

