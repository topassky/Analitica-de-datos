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
<br />
<p align="center">
  <h3 align="center">Métodos para descomposición para series temporales</h3>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Tabla de contenidos</summary>
  <ol>
    <li>
      <a>Descomposición para series estacionales</a>
    </li>
    <li>
      <a>Series sin tendencia</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## 1. Descomposición para series estacionales

Cuando la serie además de tendencia y componente aleatorio tiene estacionalidad, los métodos de descomposición suponenen que los datos se generan como suma de esos tres efectos:

```math
z_{t}=\mu_{t}+S_{t}+a_{t}
```

donde ![equation](https://latex.codecogs.com/svg.image?\mu_{t}) es el nivel de la serie, ![equation](https://latex.codecogs.com/svg.image?S_{t}) es el componente estacional y ![equation](https://latex.codecogs.com/svg.image?a_{t}) es el componente puramente aleatorio o innovación que, como modelos anteriores, es una secuencia de variables incorreladas de media cero y varianza constante. Los métodos clásicos de descomposición suponen que tanto el nivel como la estacionalidad son deterministas. El nivel ![equation](https://latex.codecogs.com/svg.image?\mu_{t}) se modela mediante un polinomio del tiempo de orden menor o iguual a dos, y la estacionalidad como una función periódica, que verifica la condición:

```math
S_{t} = S_{t-s}
```
## 2. Series sin tendencia.
Se estima el nivel de la serie observada como un modelo de tendencias deterministas. La forma de la tendencia se elige con el gráfico de la serie  y se estima como una función conocida determinista del tiempo que depende del instante conocido y de un vector de parámetros, ![equation](https://latex.codecogs.com/svg.image?\beta%20=%20%3C\beta_{0},%20\beta_{1},%20\beta_{2}%3E)

```math
\mu_{t} = f(t,\beta)
```

Un modelos más general, que se aplica a series que tienen tendencia, creciente o decreciente, es el modelo de tendencia lineal.

```math
\mu_{t} = \beta_{0} + \beta_{1}t 
```

donde,
```math
\beta_{0} = \bar{z_{t}}
```
Además
```math
\beta_{1} = \frac{\sum_{t=1}^{T}(z_{t}-\beta_{0})t}{\sum_{t=1}^{T}t^{2}}
```

<p align="center">
   <a href="https://github.com/topassky/M-todo-de-descomposici-n-para-series-estacionales.git">
    <img src="https://comcop.co/Arg/img/serie_sin_tendencia.png" alt="Logo" width="640" height="420">
  </a>
  <h3 align="center">Figura 1: Serie sin tendencia, ejemplo de base de datos parados.dat</h3>
</p>

### Prerequisitos

Para ejecutar el proyecto debes instalar las siguientes librerias:
* opencv
  ```sh
  pip install opencv-python
  ```
* opencv-contrib-python
  ```sh
  pip install opencv-contrib-python
  ```
* imutils
  ```sh
  pip install imutils
  ```
* pyzbar
  
  Se recomienda ver la socumentación oficial de la libreria.



