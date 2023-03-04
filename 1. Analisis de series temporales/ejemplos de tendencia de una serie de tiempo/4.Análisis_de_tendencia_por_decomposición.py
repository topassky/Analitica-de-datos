"""
Análisis de tendencia por decomposición: Este método implica descomponer una serie 
de tiempo en sus componentes estacional, cíclico y tendencia. Es útil para identificar 
y analizar los diferentes elementos que contribuyen a la serie de tiempo.

En este ejemplo, se crea un DataFrame con una serie de tiempo de fechas y valores. 
Se convierte la columna 'fecha' en una fecha y se establece como índice del DataFrame. 
Se utiliza el método seasonal_decompose() para descomponer la serie de tiempo en sus 
componentes estacional, cíclico y tendencia. y se imprime la tendencia de la serie de tiempo. 
En este caso, como la serie de tiempo es simple, no se puede observar tendencia, 
pero en una serie de tiempo real se debe tener en cuenta mas factores como la estacionalidad 
y la heterocedasticidad, además es recomendable utilizar validación cruzada para obtener 
un modelo mas robusto.
"""

import statsmodels.api as sm
import pandas as pd

# Crear un DataFrame con una serie de tiempo
data = {'fecha': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
        'valor': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Convertir la columna 'fecha' en una fecha
df['fecha'] = pd.to_datetime(df['fecha'])

# Establecer la columna 'fecha' como índice del DataFrame
df.set_index('fecha', inplace=True)

# Decomposición de la serie de tiempo
result = sm.tsa.seasonal_decompose(df['valor'], model='additive')

# Imprimir la tendencia de la serie de tiempo
print(result.trend)