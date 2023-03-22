<h1 align="center"> Procesos estocásticos</h1>

<p align="justify">Un proceso estocástico es un fenómeno en el que las variables aleatorias <img src = "https://latex.codecogs.com/svg.image?Z_{T}"> toman valores en un conjunto ordenado de instantes temporales (días, meses, años, etc). Cada uno de estos instantes está representado por una variable aleatoria <img src = "https://latex.codecogs.com/svg.image?z_{T}"> y la combinación de todas las variables aleatorias observadas en cada instante forma una serie temporal. Esta serie temporal es una muestra de tamaño uno del vector de variables aleatorias ordenadas en el tiempo y se considera una realización o trayectoria del proceso estocástico.</p> 

<p align="justify">El proceso estocástico se puede caracterizar definiendo la distribución de probabilidad conjunta de todas las variables aleatorias <img src="https://latex.codecogs.com/svg.image?(z_{1},&space;...,&space;z_{t},&space;...,&space;z_{T})"> para cualquier valor de T. Estas distribuciones se conocen como distribuciones finito dimensionales del proceso. Se dice que conocemos la estructura probabilística del proceso estocástico cuando conocemos estas distribuciones, las cuales determinan la distribución de cualquier subconjunto de variables y, en particular, las distribuciones marginales de cada variable individual.</p> 

<p align="justify">Por ejemplo, si consideramos una variable climática, como la cantidad de lluvia, la humedad o la contaminación, en una ciudad específica, registrada a las 12 horas de cada día durante un año, las 365 observaciones recogidas para esa variable representan una realización del proceso estocástico. Al comenzar un nuevo año, se obtiene una nueva realización del proceso estocástico y así sucesivamente. Si examinamos el valor de la variable en el día 9 de junio de diferentes años, tendremos la distribución de probabilidad de una variable aleatoria. </p> 

<p align="justify">La figura 1 presenta 12 realizaciones (años) de la serie de lluvia en Madrid en los 12 meses del año. Hay 12 valores de 12 variables aleatorias, una para cada mes, y la trayectoria de los 12 valores en un año determinado representa una realización del proceso estocástico. Si se considera un mes cualquiera, los 12 valores disponibles forman una muestra de tamaño 12 de una variable aleatoria.</p>

<p align="center"><img src="https://github.com/topassky/Analitica-de-datos/blob/master/3.%20Procesos%20estocasticos/Figure_1.png"> </p>

<p align="justify">Como segundo ejemplo, se considera un proceso estocástico definido por:</p>

<p align="center"><img src="https://latex.codecogs.com/svg.image?z_{t}=z_{t-1}&plus;a_{t}"></p>

<p align="justify">Se supone que este proceso estocástico comienza en un instante <img src="https://latex.codecogs.com/svg.image?t=0"> con <img src="https://latex.codecogs.com/svg.image?z_{0}=0">, y que las variables <img src="https://latex.codecogs.com/svg.image?a_{t}"> son normales con media cero y varianza constante <img src="https://latex.codecogs.com/svg.image?\sigma&space;^{2}"> a lo largo del tiempo, e independientes entre sí. Este proceso es conocido como "paseo aleatorio" y la figura 2 presenta 200 realizaciones de este proceso generadas por un ordenador. El proceso siempre comienza con el valor 0, pero se aleja de él a medida que avanza el tiempo.</p> 

<p align="center"><img src="https://github.com/topassky/Analitica-de-datos/blob/master/3.%20Procesos%20estocasticos/Figure_2.png"> </p>


<p align="justify">La figura 3 presenta histogramas de la distribución de los 200 valores de la variable del proceso en los tiempos t = 25, 50, 75 y 100. Se puede apreciar que, aunque la media de estas distribuciones es aproximadamente cero en los cuatro casos, la varianza de la distribución aumenta a medida que avanza el tiempo. Este resultado coincide con lo que se muestra en la figura 2, en la que se puede ver que las realizaciones del proceso tienden a alejarse del valor inicial con el paso del tiempo.</p>

<p align="center"><img src="https://github.com/topassky/Analitica-de-datos/blob/master/3.%20Procesos%20estocasticos/Figure_3.png"> </p>

<p align="justify">Se puede observar que existen varias realizaciones de un proceso estocástico en fenómenos estables y repetitivos a lo largo del tiempo. Por ejemplo, en variables climáticas, astronómicas o ambientales que siguen cada año un patrón similar debido a la rotación de la tierra alrededor del sol. Además, en variables que se repiten en las mismas condiciones, como el ritmo cardiovascular de una persona a lo largo del día (en días similares) o el rendimiento obtenido por una acción en diferentes días, entre otros. Si se define la ecuación de generalización de las observaciones de un proceso, se pueden generar todas las realizaciones deseadas en un ordenado.</p>

<p align="justify">Para determinar la distribución conjunta del proceso, es necesario observar un gran número de realizaciones con el fin de estimar la probabilidad de los distintos intervalos. Esta tarea se simplifica considerablemente cuando se puede suponer que la distribución conjunta es normal multivariable, ya que en ese caso, se determinará por el vector de medias y la matriz de varianzas y covarianzas entre las variables.</p>

<h2>Propiedades de las distribuciones marginales</h1>

<p align="justify">Se llama funciones de medias del proceso a una función en el tiempo que proporciona la esperanza de las distribuciones marginales <img src="https://latex.codecogs.com/svg.image?z_{t}"> en cada instante. Esto se define como: .</p>

<p align="center"><img src="https://latex.codecogs.com/svg.image?E[z_{t}]&amp;space;=&amp;space;\mu_{t}"></p>

<p align="justify">Un caso particular importante, por su simplicidad, aparece cuando todas las variables tienen la misma media. En este caso, la función de medias es constante. Las realizaciones del proceso no mostrarán ninguna tendencia y se dice que el proceso es estable en la media. Si por el contrario, las medias cambian en el tiempo, las variaciones de dicho proceso mostrarán dicho cambio. Por ejemplo, en el caso del proceso estocástico producido por un ordenador, se ha demostrado que los histogramas en el tiempo t tienen una media de 0. Esto se puede deducir con los siguientes cálculos matemáticos. </p>

<p align="center"><img src="https://latex.codecogs.com/svg.image?E[z_{1}]=0&plus;E[a_{1}]=0&space;"></p>

<p align="justify">Además, se puede utilizar el hecho de que si la esperanza de <img src="https://latex.codecogs.com/svg.image?z_{t-1}&amp;space;"> es cero, también lo es la de <img src="https://latex.codecogs.com/svg.image?z_{t}">, ya que: </p>

<p align="center"><img src="https://latex.codecogs.com/svg.image?E[z_{t}]=E[z_{t-1}]&amp;plus;E(a_{t})=0&amp;space;"></p>

<p align="justify">Como segundo ejemplo, se tiene la serie de lluvias que, como se evidencia en la figura 4, no tiene una media constante, ya que la cantidad media de lluvia varía en los diferentes meses del año. </p>

<p align="center"><img src="https://github.com/topassky/Analitica-de-datos/blob/master/3.%20Procesos%20estocasticos/Figure_4.png"></p>

<p align="justify">Se denominan funciones de varianzas del proceso a aquellas que proporcionan las varianzas en cada instante temporal.  </p>

<p align="center"><img src="https://latex.codecogs.com/svg.image?Var(z_{t})=\sigma_{t}^{2}&amp;space;"></p>

<p align="justify">Se dice que un proceso es estable en la varianza si su varianza es constante en el tiempo. Es posible que un proceso sea estable en la media y no en la varianza, o viceversa. Por ejemplo, en el caso del proceso aleatorio creado por un computador, se ha demostrado que su media es constante, pero su varianza no es constante en el tiempo. Por lo tanto, si se supone que la varianza de <img src="https://latex.codecogs.com/svg.image?a_{t}">  es <img src="https://latex.codecogs.com/svg.image?\sigma^{2}&amp;space;">, entonces la variable <img src = "https://latex.codecogs.com/svg.image?z_{2}"> cumplirá con:</p>

<p align="center"><img src="https://latex.codecogs.com/svg.image?Var(z_{2})=E(z_{2}^{2})=E(z_{1}^{2}&plus;a_{2}^{2}&plus;2z_{1}a_{2})=2\sigma^{2}"></p>

<p align="justify">Dado que la variable <img src="https://latex.codecogs.com/svg.image?z_{1}"> depende únicamente de <img src="https://latex.codecogs.com/svg.image?a_{1}">, la cual es independiente de a2, se puede afirmar que las variables z1 y a2 son independientes. Si se aplica esta ecuación sucesivamente para t=3,4,..., se puede deducir con facilidad que la varianza de zt es igual a tsigm^2. Es importante destacar que la varianza de zt aumenta de manera lineal con el tiempo.</p>















