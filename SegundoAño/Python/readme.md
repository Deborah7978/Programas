# 10-prediccion_calidad_vino.py
##Análisis de Calidad del Vino con Modelos de Regresión

Este ejercicio presenta un análisis de datos y modelado predictivo utilizando un conjunto de datos sobre la calidad del vino. El objetivo principal es predecir la calidad del vino basándose en diversas características químicas y físicas.

*Puntos iniciales empleados:
1. Exploración de Datos.
2. Preprocesamiento.
3. Modelo predictivo.
   • Árbol de Decisión.
   • Random Forest.
4. Evaluación del Modelo.
5. Importancia de Características.

*Herramientas utilizadas
• Pandas: Para la manipulación y análisis de datos.
• Matplotlib y Seaborn: Para la visualización de datos.
• Scikit-learn: Para el preprocesamiento, modelado y evaluación.

Este ejercicio proporciona una comprensión práctica de cómo aplicar técnicas de machine learning para resolver problemas del mundo real, específicamente en el contexto de la industria vitivinícola.

# 11-metodo_codo.py
## Método del Codo para Estimación del Número de Clústeres
Este proyecto implementa el método del codo para estimar el número óptimo de clústeres en el algoritmo k-means.
El método del codo es una técnica visual que ayuda a determinar cuántos clústeres son apropiados para un conjunto de datos dado. Se calcula la suma de errores cuadráticos (SSE) para diferentes valores de k y se grafica para identificar el "codo".

## Requisitos
- Python 3.x
- scikit-learn
- matplotlib
- numpy

# 12-comparacion_pandas_vs_polars.py
## Comparación entre Pandas y Polars

Este repositorio contiene ejemplos de uso de las bibliotecas de tratamiento de datos Pandas y Polars. Ambos son potentes herramientas para la manipulación y análisis de datos en Python, pero tienen diferentes características que pueden hacer que uno sea más adecuado que el otro dependiendo del caso de uso.

## Ventajas y Desventajas
### Pandas
*Ventajas:*
- *Madurez y Comunidad:* Pandas es una biblioteca muy establecida con una gran comunidad y abundante documentación.
- *Funcionalidad Completa:* Ofrece una amplia gama de funcionalidades para manipulación de datos, incluyendo manejo de fechas, operaciones de fusión, entre otros.
- *Integración con otras bibliotecas:* Se integra bien con otras bibliotecas populares en el ecosistema de Python como NumPy, Matplotlib y Scikit-learn.

*Desventajas:*
- *Rendimiento:* Puede ser más lento en comparación con Polars al trabajar con conjuntos de datos muy grandes, especialmente cuando se trata de operaciones complejas.
- *Uso de Memoria:* Consume más memoria debido a su diseño basado en objetos.

### Polars
*Ventajas:*
- *Rendimiento:* Diseñado para ser rápido y eficiente en memoria, especialmente en operaciones sobre grandes volúmenes de datos.
- *Paralelismo:* Utiliza paralelismo para acelerar las operaciones, lo que puede resultar en un rendimiento significativamente mejor en comparación con Pandas.
- *Interfaz Similar:* Tiene una API similar a la de Pandas, lo que facilita la transición para los usuarios familiarizados con Pandas.

*Desventajas:*
- *Menos Madura:* Es una biblioteca más nueva y puede carecer de algunas funcionalidades avanzadas que están presentes en Pandas.
- *Documentación Limitada:* Aunque está mejorando, la documentación y los recursos pueden no ser tan abundantes como los de Pandas.

# 13-conjunto_datos_minist.py

Este proyecto utiliza el conjunto de datos MNIST, que contiene imágenes de dígitos manuscritos del 0 al 9, para construir y entrenar un modelo de red neuronal utilizando TensorFlow y Keras. A continuación, se describen los pasos realizados en el código.

1. Cargar el Dataset MNIST
Se carga el conjunto de datos MNIST utilizando la función load_data() de Keras. Este conjunto de datos se divide en dos partes: un conjunto de entrenamiento y un conjunto de prueba.

2. Normalizar los Datos
Los valores de los píxeles de las imágenes se normalizan a un rango de 0 a 1 dividiendo por 255.0. Esto ayuda a mejorar la convergencia del modelo durante el entrenamiento.

3. One-Hot Encoding de las Etiquetas
Las etiquetas de clase se convierten a un formato de codificación one-hot utilizando la función to_categorical(). Esto es necesario para que el modelo pueda aprender a clasificar correctamente las imágenes.

4. Crear el Modelo Secuencial
Se define un modelo secuencial que consiste en varias capas:
• Capa de entrada: Flatten, que convierte las imágenes de 28x28 píxeles en vectores de 784 elementos.
• Capa oculta 1: Dense con 256 neuronas y activación ReLU.
• Dropout: Se aplica una capa de Dropout con una tasa del 30% para evitar el sobreajuste.
• Capa oculta 2: Otra capa Dense con 128 neuronas y activación ReLU.
• Capa de salida: Dense con 10 neuronas y activación softmax para clasificar los dígitos.
    
5. Compilar el Modelo
El modelo se compila utilizando el optimizador Adam y la función de pérdida categorical_crossentropy, además de establecer la métrica de precisión para evaluar el rendimiento.

6. Early Stopping para Evitar Sobreentrenamiento
Se implementa el mecanismo de EarlyStopping para detener el entrenamiento si la pérdida de validación no mejora después de 3 épocas, lo que ayuda a prevenir el sobreentrenamiento.

7. Entrenar el Modelo
El modelo se entrena durante 15 épocas con un tamaño de lote de 32, utilizando un 10% de los datos de entrenamiento para validación.

8. Evaluar el Modelo en el Conjunto de Prueba
Se evalúa el rendimiento del modelo en el conjunto de prueba y se imprime la pérdida y precisión obtenidas.

9. Graficar la Precisión y la Pérdida
Finalmente, se grafican las métricas de precisión y pérdida tanto para el conjunto de entrenamiento como para el de validación a lo largo de las épocas.