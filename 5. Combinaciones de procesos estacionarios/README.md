<h1 align="center">Combinaciones de procesos estacionarios</h1>

<p align="justify">Se denomina matriz de covarianzas del proceso estacionario de orden k a la matriz cuadrada y simétrica de orden k que presenta en su diagonal principal las varianzas y en las diagonales siguientes las autocovarianzas. Esta definición establece que la matriz <img src="https://latex.codecogs.com/svg.image?&space;\Gamma_{k}"> se define por la relación entre las autocovarianzas y varianzas de un proceso estacionario. Además, se puede afirmar que esta matriz proporciona información valiosa sobre la estructura y dependencias del proceso estacionario.<p>

<p align="center"><img src="https://latex.codecogs.com/svg.image?\Gamma_{k}&space;=&space;E[\begin{bmatrix}z_{t}&space;-&space;\mu&space;\\z_{t-1}&space;-&space;\mu\\z_{t-2}&space;-&space;\mu\end{bmatrix}&space;\begin{bmatrix}&space;z_{t}-\mu&space;&&space;z_{t-1}-\mu&space;&&space;z_{t-2}-\mu&space;\\\end{bmatrix}]"> </p>

<p align="justify">La función de autocrrelación simple (FAS) se refiere a la representación de las autorrelaciones de un proceso en función al retardo. Por otro lado, la matriz de autocrrelación es una matriz cuadrada y simétrica con unos en la diagonal y los coeficientes de autocorrelación fuera de la diagonal.<p>
  
<p align="center"><img src="https://latex.codecogs.com/svg.image?R_{k}&space;=&space;\begin{bmatrix}1&space;&&space;\rho_{1}&space;&space;&&space;\rho_{k-1}&space;&space;\\\rho_{1}&space;&&space;1&space;&&space;\rho_{k-2}&space;\\\rho_{k-1}&space;&&space;\rho_{k-2}&space;&&space;1&space;\\\end{bmatrix}">  </p>

<p align="justify">Una propiedad importante de los procesos estacionarios es que son estables ante combinaciones lineales. Esto significa que los procesos obtenidos mediante combinaciones lineales de procesos estacionarios son también estacionarios. En particular, la combinación lineal formada por los incrementos de un proceso estacionario es una serie estacionaria. En otras palabras, si <img src="https://latex.codecogs.com/svg.image?z_{t}"> es estacionario, el proceso <img src="https://latex.codecogs.com/svg.image?w_{t}"> definido por:  <p>
  
<p align="center"><img src="https://latex.codecogs.com/svg.image?\omega_{t}=z_{t}-z_{t-1}">  </p>

<p align="justify">Efectivamente, se procederá a verificar las tres condiciones de la sección anterior para determinar la estacionalidad en sentido débil. Es fácil constatar que la esperanza de <img src="https://latex.codecogs.com/svg.image?\omega_{t}">  siempre es cero. La varianza será constante, puesto que, al denominar <img src="https://latex.codecogs.com/svg.image?\sigma&amp;space;^{2}"> a la varianza de <img src="https://latex.codecogs.com/svg.image?&amp;space;z_{t}"> y <img src="https://latex.codecogs.com/svg.image?\gamma_{1}"> a la covarianza entre observaciones contiguas: </p>

<p align="center"><img src="https://latex.codecogs.com/svg.image?Var(\omega_{t})=Var(z_{t})+Var(z_{t-1})-2Cov(z_{t},z_{t-1})=2(\sigma^{2}-\gamma_{1})">  </p>

<p align="justify">que no depende de t. en tercer lugar, su función de autocovarianzaes: </p>

<p align="center"><img src="https://latex.codecogs.com/svg.image?cov(\omega_{t},\omega_{t&amp;plus;k})=E[(z_{t}-z_{t-1})(z_{t&amp;plus;k}-z_{t&amp;plus;k-1})]=2\gamma_{k}-\gamma_{k&amp;plus;1}-\gamma_{k-1}&amp;space;">  </p>

<p align="justify"> Se procederá a demostrar el resultado general de que toda combinación lineal de procesos estacionarios es un nuevo proceso estacionario (esta prueba puede omitirse sin pérdida de continuidad). Supongamos que <img src="https://latex.codecogs.com/svg.image?z_{t}&amp;space;=&amp;space;(z_{1t},...,z_{kt})"> es un vector de k procesos estacionarios, donde se asume que las autocovarianzas entre dos componentes en dos instantes de tiempo solo dependen de los dos componentes considerados y del retardo entre los instantes temporales. Bajo estas condiciones, el vector de series es estacionario. Ahora, considérese el proceso escalar definido por el vector de constantes <img src="https://latex.codecogs.com/svg.image?c'&amp;space;=&amp;space;(c_{1},...,c_{2}).">  </p>


<p align="justify"> Este proceso será una combinación lineal de los componentes del vector <img src="https://latex.codecogs.com/svg.image?z_{t}">. La esperanza del proceso estacionario resultante se expresa como sigue: </p>

<p align="center"><img src="https://latex.codecogs.com/svg.image?E(y_{t})=c_{1}E(z_{1t})&amp;plus;...&amp;plus;c_{k}E(z_{kt})=c^{'}\mu&amp;space;">  </p>

<p align="justify"> Donde u=(u1,...,uk) es el vector de las medidas de los componentes. Dado que las esperanzas E(z_{it}) = ui son constantes, también lo es E{yk}. La varianza del proceso yk se calculará de la siguiente manera: </p>

<p align="center"><img src="https://latex.codecogs.com/svg.image?var(y_{k})=E(c^{'}(z_{t}-\mu)(z_{t}-\mu)^{'}c)=c^{'}\Gamma_{z}c">  </p>

<p align="justify">  Donde <img src="https://latex.codecogs.com/svg.image?\Gamma_{z}&amp;space;"> es la matriz de covarianzas entre los componentes del vector en el mismo instante. Debido a que los componentes son estacionarios, la matriz de covarianzas entre ellos también es constante. Análogamente, se verifica que: </p>

<p align="justify">  Donde <img src="https://latex.codecogs.com/svg.image?\Gamma_{z}&amp;space;"> contiene las covarianzas entre los componentes en distintos instantes que, según la hipótesis, solo dependen del retardo. Por lo tanto, el proceso <img src="https://latex.codecogs.com/svg.image?y_{k}"> es estacionario. </p>








