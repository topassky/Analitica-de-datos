from calculo_estacionalidad.estacionalidad import Estacionalidad
from calculo_nivel_serie.nivel_serie import Nivel_serie
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Lectura del archivo de datos en formato tabla
df = pd.read_table("base_datos/tempsantiago.dat", header=None, sep='\s+')

# Se segmenta el número de la variable 'serie_original'.
tiempo = np.linspace(1, len(df[0]), len(df[0]))
serie_original = df[0]

# Se define la clase Nivel_serie
nivel_serie = Nivel_serie(tiempo, serie_original)

# Se calcula la tendencia de la serie temporal utilizando el método de media móvil
tendencia = nivel_serie.caculco_media_movil()

# Se calcula la serie sin tendencia
E_t = serie_original - tendencia 

# Se define la clase Nivel_serie para la serie sin tendencia
nivel_serie_Et = Nivel_serie(tiempo, E_t)

# Se calcula la tendencia de la serie sin tendencia utilizando el método de media móvil
tendencia_Et = nivel_serie_Et.caculco_media_movil()

# Se define la clase Estacionalidad para la serie sin tendencia
Estacionalidad = Estacionalidad(E_t, tiempo)

# Se calcula la estacionalidad con periodo 12
S_t = Estacionalidad.calculo(periodo=12)

# Se crean las cuatro subgráficas para visualizar las series temporales
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, sharex=True)
ax1.plot(tiempo, serie_original, linewidth=2.0)
ax1.plot(tiempo, tendencia, linewidth=2.0)
ax1.set_title('Serie y su tendencia')
ax2.plot(tiempo, E_t, linewidth=2.0)
ax2.set_title('Serie sin tedencia')
ax3.plot(tiempo, S_t, linewidth=2.0)
ax3.set_title('Estacionalidad')
ax4.plot(tiempo, serie_original, linewidth=2.0)
ax4.plot(tiempo, S_t+tendencia, linewidth=2.0)
ax4.set_title('Serie y descompisción de la serie')

# Se muestra la gráfica
plt.show()