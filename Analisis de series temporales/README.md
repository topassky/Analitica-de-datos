<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<h1 align="center">Métodos para descomposición para series temporales</h1>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Tabla de contenidos</summary>
  <ol>
    <li>
      <a>1. Descomposición para series estacionales</a>
    </li>
    <li>
      <a>2. Series sin tendencia</a>
    </li>
    <li>
      <a>3. Referencias</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
<h1> 1. Descomposición para series estacionales</h1>

Cuando la serie además de tendencia y componente aleatorio tiene estacionalidad, los métodos de descomposición suponenen que los datos se generan como suma de esos tres efectos: <

```math
z_{t}=\mu_{t}+S_{t}+a_{t}
```

<center>
donde <a href="https://latex.codecogs.com/svg.image?\mu_{t}">Enlace a mu_t</a> es el nivel de la serie, ![equation](https://latex.codecogs.com/svg.image?S_{t}) es el componente estacional y ![equation](https://latex.codecogs.com/svg.image?a_{t}) es el componente puramente aleatorio o innovación que, como modelos anteriores, es una secuencia de variables incorreladas de media cero y varianza constante. Los métodos clásicos de descomposición suponen que tanto el nivel como la estacionalidad son deterministas. El nivel ![equation](https://latex.codecogs.com/svg.image?\mu_{t}) se modela mediante un polinomio del tiempo de orden menor o iguual a dos, y la estacionalidad como una función periódica, que verifica la condición:
</center>

```math
S_{t} = S_{t-s}
```




