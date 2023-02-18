
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

donde <img src = "https://latex.codecogs.com/svg.image?\mu_{t}">  es el nivel de la serie, ![equation](https://latex.codecogs.com/svg.image?S_{t}) es el componente estacional y ![equation](https://latex.codecogs.com/svg.image?a_{t}) es el componente puramente aleatorio o innovación que, como modelos anteriores, es una secuencia de variables incorreladas de media cero y varianza constante. Los métodos clásicos de descomposición suponen que tanto el nivel como la estacionalidad son deterministas. El nivel ![equation](https://latex.codecogs.com/svg.image?\mu_{t}) se modela mediante un polinomio del tiempo de orden menor o iguual a dos, y la estacionalidad como una función periódica, que verifica la condición:


```math
S_{t} = S_{t-s}
```




