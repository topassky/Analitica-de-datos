<h1 align="center"> Procesos estocásticos</h1>

<p align="justify">Un proceso estocástico es un fenómeno en el que las variables aleatorias <img src = "https://latex.codecogs.com/svg.image?Z_{T}"> toman valores en un conjunto ordenado de instantes temporales (días, meses, años, etc). Cada uno de estos instantes está representado por una variable aleatoria <img src = "https://latex.codecogs.com/svg.image?z_{T}"> y la combinación de todas las variables aleatorias observadas en cada instante forma una serie temporal. Esta serie temporal es una muestra de tamaño uno del vector de variables aleatorias ordenadas en el tiempo y se considera una realización o trayectoria del proceso estocástico.</p> 

<p align="justify">El proceso estocástico se puede caracterizar definiendo la distribución de probabilidad conjunta de todas las variables aleatorias <img src="https://latex.codecogs.com/svg.image?(z_{1},&space;...,&space;z_{t},&space;...,&space;z_{T})"> para cualquier valor de T. Estas distribuciones se conocen como distribuciones finito dimensionales del proceso. Se dice que conocemos la estructura probabilística del proceso estocástico cuando conocemos estas distribuciones, las cuales determinan la distribución de cualquier subconjunto de variables y, en particular, las distribuciones marginales de cada variable individual.</p> 

<p align="justify">Por ejemplo, si consideramos una variable climática, como la cantidad de lluvia, la humedad o la contaminación, en una ciudad específica, registrada a las 12 horas de cada día durante un año, las 365 observaciones recogidas para esa variable representan una realización del proceso estocástico. Al comenzar un nuevo año, se obtiene una nueva realización del proceso estocástico y así sucesivamente. Si examinamos el valor de la variable en el día 9 de junio de diferentes años, tendremos la distribución de probabilidad de una variable aleatoria. </p> 

<p align="justify">La figura 1 presenta 12 realizaciones (años) de la serie de lluvia en Madrid en los 12 meses del año. Hay 12 valores de 12 variables aleatorias, una para cada mes, y la trayectoria de los 12 valores en un año determinado representa una realización del proceso estocástico. Si se considera un mes cualquiera, los 12 valores disponibles forman una muestra de tamaño 12 de una variable aleatoria.</p>

<p align="center"><img src="https://github.com/topassky/Analitica-de-datos/blob/master/3.%20Procesos%20estocasticos/Figure_1.png"> </p>

<p align="justify">Como segundo ejemplo, se considera un proceso estocástico definido por:</p>

<p align="center">< img src="https://latex.codecogs.com/svg.image?z_{t}=z_{t}&plus;a_{t}"></p>

<p align="center">Se supone que este proceso estocástico comienza en un instante <img src="https://latex.codecogs.com/svg.image?t=0"> con < img src="https://latex.codecogs.com/svg.image?z_{0}=0">, y que las variables at son normales con media cero y varianza constante <img src="https://latex.codecogs.com/svg.image?\sigma&space;^{2}"> a lo largo del tiempo, e independientes entre sí. Este proceso es conocido como "paseo aleatorio" y la figura 2 presenta 200 realizaciones de este proceso generadas por un ordenador. El proceso siempre comienza con el valor 0, pero se aleja de él a medida que avanza el tiempo.</p> 
