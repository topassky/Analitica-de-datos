
<!-- PROJECT LOGO -->
<h1 align="center">Métodos para descomposición para series temporales</h1>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Tabla de contenidos</summary>
  <ol>
    <li>
      Descomposición para series estacionales
    </li>
    <li>
      Series sin tendencia
    </li>
    <li>
      Referencias
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
<h2> 1. Descomposición para series estacionales</h2>

<p>Cuando la serie además de tendencia y componente aleatorio tiene estacionalidad, los métodos de descomposición suponenen que los datos se generan como suma de esos tres efectos:</p> 

<p align="center"> <img src="https://latex.codecogs.com/svg.image?z_{t}=\mu_{t}+S_{t}+a_{t}" alt="Expresión matemática"> </p>

<p align="justify"> Donde <img src = "https://latex.codecogs.com/svg.image?\mu_{t}">  es el nivel de la serie, <img src = "https://latex.codecogs.com/svg.image?S_{t}"> es el componente estacional y <img src=https://latex.codecogs.com/svg.image?a_{t}> es el componente puramente aleatorio o innovación que, como modelos anteriores, es una secuencia de variables incorreladas de media cero y varianza constante. Los métodos clásicos de descomposición suponen que tanto el nivel como la estacionalidad son deterministas.

<h3>1.1 Calculo de del nivel de la serie por el método de media_movil.</h3>

<p align="justify">Este método implica el cálculo de la media de un número específico de puntos de datos consecutivos y trazar una línea a través de esos puntos medios. El resultado es una serie suavizada que muestra el patrón general de la tendencia de la serie. </p>

<p align="justify"> En el proceso de cálculo, primero se crea un DataFrame con la serie temporal de fechas y valores. Luego, se convierte la columna 'fecha' en una fecha y se establece como índice del DataFrame. Se utiliza el método rolling() para calcular la media móvil de un número determinado de días y se almacena el resultado en una nueva columna llamada 'media_movil'.</p>

<p align="justify"> Es importante tener en cuenta que los primeros valores de la columna 'media_movil' pueden estar vacíos debido a que no hay suficientes datos para calcular la media móvil en esos puntos. Para manejar estos valores faltantes, se pueden utilizar diferentes métodos de interpolación o de llenado de datos. </p>






