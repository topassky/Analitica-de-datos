
<!-- ABOUT THE PROJECT -->
<h1 align="center"> Descomposición para series estacionales</h1>

<p>Cuando la serie además de tendencia y componente aleatorio tiene estacionalidad, los métodos de descomposición suponenen que los datos se generan como suma de esos tres efectos:</p> 

<p align="center"> <img src="https://latex.codecogs.com/svg.image?z_{t}=\mu_{t}+S_{t}+a_{t}" alt="Expresión matemática"> </p>

<p align="justify"> Donde <img src = "https://latex.codecogs.com/svg.image?\mu_{t}">  es el nivel de la serie, <img src = "https://latex.codecogs.com/svg.image?S_{t}"> es el componente estacional y <img src=https://latex.codecogs.com/svg.image?a_{t}> es el componente puramente aleatorio o innovación que, como modelos anteriores, es una secuencia de variables incorreladas de media cero y varianza constante. Los métodos clásicos de descomposición suponen que tanto el nivel como la estacionalidad son deterministas.

<h2>1. Cálculo de del nivel de la serie por el método de media_movil.</h2>

<p align="justify">Este método implica el cálculo de la media de un número específico de puntos de datos consecutivos y trazar una línea a través de esos puntos medios. El resultado es una serie suavizada que muestra el patrón general de la tendencia de la serie. </p>

<p align="justify"> En el proceso de cálculo, primero se crea un DataFrame con la serie temporal de fechas y valores. Luego, se convierte la columna 'fecha' en una fecha y se establece como índice del DataFrame. Se utiliza el método rolling() para calcular la media móvil de un número determinado de días y se almacena el resultado en una nueva columna llamada 'media_movil'.</p>

<p align="justify"> Es importante tener en cuenta que los primeros valores de la columna 'media_movil' pueden estar vacíos debido a que no hay suficientes datos para calcular la media móvil en esos puntos. Para manejar estos valores faltantes, se pueden utilizar diferentes métodos de interpolación o de llenado de datos. </p>

<h2>2. Cálculo de del nivel de la serie por el método de regresión lineal.</h2>

<p align="justify">El cálculo del nivel de la serie por el método de regresión lineal es una técnica utilizada en el análisis de series temporales para estimar la tendencia en una serie de datos a lo largo del tiempo. Este método consiste en ajustar una línea recta a los datos y utilizar la pendiente de la línea como una medida de la tasa de cambio a lo largo del tiempo. El valor de la intersección de la línea con el eje vertical se interpreta como el nivel de la serie en el momento inicial. Al igual que otros métodos de análisis de series temporales, este método asume que los datos están libres de patrones estacionales o cíclicos, y que la relación entre la variable dependiente y el tiempo es lineal. </p>

<h2>3. Cálculo de del nivel de la serie por el método de análisis de tendencia por diferenciación.</h2>

<p align="justify">Este método se basa en la diferenciación de la serie temporal para obtener una nueva serie sin la componente de tendencia. Se calcula la primera o segunda diferencia de la serie original y se ajusta un modelo de regresión lineal simple a la serie diferenciada. El coeficiente de la variable temporal en el modelo ajustado se interpreta como la tasa de cambio de la serie en el tiempo y representa la estimación del nivel de la serie. Este método es útil cuando la serie temporal no presenta una tendencia clara y se busca estimar el nivel de la serie a partir de la tasa de cambio de la misma.</p>




