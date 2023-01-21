"""
'Según el modelo de lenguaje ChatGPT de OpenAI,'

Análisis de tendencia por diferenciación: Este método implica calcular la 
diferencia entre valores consecutivos en la serie de tiempo y trazar una 
línea a través de esos puntos de diferencia. Es útil para identificar tendencias 
estacionales y cambios en la tendencia.

En este ejemplo, se crea un DataFrame con una serie de tiempo de fechas y valores. 
Se convierte la columna 'fecha' en una fecha y se establece como índice del DataFrame. 
Se utiliza el método diff() para calcular la diferencia entre valores consecutivos en 
la serie de tiempo y se almacena el resultado en una nueva columna llamada 'diferencia'. 
En este caso, la tendencia es constante y positiva con un valor de 1, lo cual puede 
indicar una tendencia al alza.

Ten en cuenta que este ejemplo es para una serie de tiempo simple, en una serie de 
tiempo real, se deben tener en cuenta mas factores como la estacionalidad y la 
heterocedasticidad, además es recomendable utilizar validación cruzada para obtener 
un modelo mas robusto.
"""

import pandas as pd

# Crear un DataFrame con una serie de tiempo
data = {'fecha': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
        'valor': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Convertir la columna 'fecha' en una fecha
df['fecha'] = pd.to_datetime(df['fecha'])

# Establecer la columna 'fecha' como índice del DataFrame
df.set_index('fecha', inplace=True)

# Calcular la diferencia entre valores consecutivos
df['diferencia'] = df['valor'].diff()

print(df)
