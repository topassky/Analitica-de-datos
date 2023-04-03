<h1 align="center">Procesos estacionarios</h1>

<p align="justify">En ciertas situaciones, es posible obtener las distribuciones de probabilidad de proceso, por ejemplo, con variables climáticas, donde se puede suponer que cada año se observa una relación del mismo proceso o mediante técnicas que pueden generarse en un laboratorio. Sin embargo, en muchas situaciones de interés, como en variables económicas o sociales, sólo se puede observar una realización del proceso. Por ejemplo, si se observa la serie de crecimiento anual de la riqueza de un país, no es posible volver atrás en el tiempo para generar otra realización. El proceso estocástico existe conceptualmente, pero no es posible obtener sucesivas muestras o realizaciones independientes del mismo.</p> 

<p align="justify">Para poder estimar las características "transversales" del proceso, como las medias, varianzas, etc., a partir de su evolución "longitudinal", es necesario suponer que las propiedades "transversales" (distribución de las variables en cada instante) son estables a lo largo del tiempo. Esto conduce al concepto de estacionalidad, que se define a continuación.</p> 

<ol>
  <li>Las distribuciones marginales de todas las variables son idénticas. </li>
  <li>Las distribuciones finito-dimensionales de cualquier conjunto de variables estocásticas dependen únicamente de los retardos entre ellas.</li>
</ol>

<p align="justify">En términos generales, se establece que las distribuciones marginales de todas las variables estocásticas son las mismas. Además, los coeficientes de asimetría y curtosis de estas distribuciones son iguales ya que se mantienen para todos los retardos. La segunda condición impone que la dependencia entre las variables solo depende de sus retardos, lo que significa que la misma dependencia existe entre las variables en diferentes momentos del proceso. Estas dos condiciones se pueden resumir afirmando que la distribución conjunta de cualquier conjunto de variables no cambia si se trasladan en el tiempo. En otras palabras, si tenemos una distribución conjunta <img src="https://latex.codecogs.com/svg.image?F(z_{i},z_{j},....,z_{k})"> también podemos escribirla como <img src="https://latex.codecogs.com/svg.image?F(z_{i+h},z_{j+h},...,z_{k+h})">  sin que esta se vea afectada.</p> 

<p align="center"><img src="https://latex.codecogs.com/svg.image?F(z_{i},z_{j},...,z_{k+h})=F(z_{i+h},z_{j+h},...,z_{k+h}) "></p>

<p align="justify">Se presenta un ejemplo que coprueba la función anterior que simula un proceso estocástico estacionario y verifica si cumple con las condiciones de estacionariedad. Para hacer esto, se define una función llamada generar_proceso_estacionario que crea un proceso estocástico utilizando una serie temporal autocorrelacionada con una media, desviación estándar y autocorrelación dadas. La función verificar_condiciones se encarga de comprobar si las condiciones de estacionariedad se cumplen, es decir, si las distribuciones marginales, los coeficientes de asimetría y curtosis se mantienen constantes al trasladar el proceso en el tiempo. Además el código presentado introduce una función llamada verificar_distribuciones_finito_dimensionales para analizar si las distribuciones finito-dimensionales de un proceso estocástico dependen únicamente de los retardos entre sus variables. La función evalúa la relación entre las variables estocásticas al calcular las correlaciones de Pearson para diferentes retardos en el proceso dado. Obteniedo los siguientes resultados: </p> 

<p align="center">
Condiciones cumplidas con una tolerancia de 0.01
</p> 
<p align="center">
Correlación con retardo 1 es: 0.7766326526771806
</p> 

<p align="center">
<img src="https://github.com/topassky/Analitica-de-datos/blob/master/4.%20Procesos%20estacionarios/Figure_1.png">
</p>

