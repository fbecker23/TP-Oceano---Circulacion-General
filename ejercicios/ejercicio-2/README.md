1) Descargar los campos mensuales de temperatura superficial del mar (SST) para el dominio del Pacífico ecuatorial (30°N–30°S; 120°E–60°W), desde enero de 2003 hasta diciembre de 2025 (fuente sugerida: MODIS-AQUA nivel 3, SST 11 mic, https://oceandata.sci.gsfc.nasa.gov/l3/)
  - Calcular las anomalías mensuales de SST removiendo el ciclo estacional.


2) Análisis de EOF
  - Aplicar un análisis de Funciones Ortogonales Empíricas (EOF) sobre el campo de anomalías de SST.
  - Identificar los dos primeros modos espaciales (EOF1 y EOF2) y sus respectivas series temporales (PC1 y PC2).


3) Análisis espectral del modo principal
  - Realizar un análisis espectral sobre la serie temporal del primer componente principal (PC1).
  - Determinar qué frecuencia domina (escala temporal en meses o años).


4) Identificación de fases del ENSO
  - A partir del PC1, seleccionar algunos meses representativos de las fases cálida (El Niño) y fría (La Niña).
  - Graficar los campos medios de anomalías de SST sobre el Pacífico ecuatorial para ambos conjuntos de meses.



Contenido:

- ejemplo_SST_EOF.nc : Pequeño dataset sintético de ejemplo para testeo rápido.
- ejercicios/ejercicio_2_EOF.ipynb : Notebook para el Ejercicio 2 (Para abrir el script en colab: [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fbecker23/TP-Oceano---Circulacion-General/blob/main/ejercicios/ejercicio-2/ejercicio_2_EOF.ipynb)
