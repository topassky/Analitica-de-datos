"""
'Según el modelo de lenguaje ChatGPT de OpenAI,' 

Media móvil: Este método implica calcular la media de un número específico de puntos 
de datos consecutivos y trazar una línea a través de esos puntos medios. 
Es útil para suavizar la serie de tiempo y ver el patrón general de la tendencia.

En este ejemplo, se crea un DataFrame con una serie de tiempo de fechas y valores. 
Se convierte la columna 'fecha' en una fecha y se establece como índice del DataFrame. 
Se utiliza el método rolling() para calcular la media móvil de 3 días y se almacena el 
resultado en una nueva columna llamada 'media_movil'.

Ten en cuenta que en los primeros dos valores de la columna 'media_movil' aparecen NaN
porque no hay suficientes valores para calcular la media movil en esos casos, se 
recomienda que uses diferentes métodos para manejar esos valores.
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

# Calcular la media móvil de 3 días
df['media_movil'] = df['valor'].rolling(window=3).mean()

print(df)
