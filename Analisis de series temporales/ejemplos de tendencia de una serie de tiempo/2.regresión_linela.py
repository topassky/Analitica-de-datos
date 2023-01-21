"""
'Según el modelo de lenguaje ChatGPT de OpenAI,'

Regresión lineal: Este método implica encontrar la línea de tendencia que mejor 
se ajusta a los datos mediante el uso de la ecuación de una línea recta. 
Es útil para predecir valores futuros en función de la tendencia encontrada.

En este ejemplo, se crea una serie de tiempo con los valores de x y y, 
se crea un modelo de regresión lineal y se entrena con los datos de la serie 
de tiempo. Se utiliza el método fit() para entrenar el modelo con los datos 
de la serie de tiempo. Despues se imprime el coeficiente (pendiente) y el 
intercepto de la recta de regresión, estos valores son la tendencia de la 
serie de tiempo.

Ten en cuenta que este ejemplo es solo una representación simple, 
para una serie de tiempo real, se deben tener en cuenta mas factores 
como la estacionalidad y la heterocedasticidad, además es recomendable 
utilizar validación cruzada para obtener un modelo mas robusto.
"""

from sklearn.linear_model import LinearRegression
import numpy as np

# Crear una serie de tiempo
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

# Crear un modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo con los datos de la serie de tiempo
model.fit(x.reshape(-1, 1), y)

# Obtener la pendiente (coeficiente) de la regresión lineal
print(model.coef_)

# Obtener el punto de intersección (intercepto) de la regresión lineal
print(model.intercept_)
