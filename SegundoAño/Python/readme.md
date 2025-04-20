Seminario Prático a entregar el Lunes 21 de abril de 2025 a las 12:00 M como fecha Límite.

Título del Ejercicio: Predicción de la Calidad del Vino

Enviar enlace en una rama del repositorio en el readme.md la explicación del ejercicio.

Descripción:

En este ejercicio, los estudiantes trabajarán con un conjunto de datos que contiene información sobre diversas propiedades 
químicas de diferentes vinos y su calidad correspondiente (puntuación del 0 al 10). 
El objetivo es construir modelos de Árboles de Decisión y Random Forest para predecir 
la calidad del vino basándose en sus propiedades químicas.

Conjunto de Datos:

Utilizaremos el conjunto de datos "Wine Quality", disponible en el repositorio de UCI Machine Learning (o fácilmente descargable desde Kaggle). Este conjunto de datos contiene información sobre vinos tintos y blancos. Para simplificar, nos centraremos en los vinos tintos.

Pasos del Ejercicio:

    Carga y Exploración de Datos:
        Cargar el conjunto de datos "winequality-red.csv" utilizando la librería Pandas.
        Realizar un análisis exploratorio básico: mostrar las primeras filas, estadísticas descriptivas, distribución de la variable objetivo (calidad).
        Visualizar la relación entre algunas variables y la calidad del vino (por ejemplo, usando gráficos de dispersión o boxplots).

    Preprocesamiento de Datos:
        Dividir el conjunto de datos en características (X) y variable objetivo (y).
        Dividir el conjunto de datos en conjuntos de entrenamiento y prueba.
        Estandarizar o normalizar las características si es necesario.

    Construcción de un Árbol de Decisión:
        Entrenar un modelo de Árbol de Decisión utilizando la librería Scikit-learn.
        Evaluar el rendimiento del modelo en el conjunto de prueba (por ejemplo, utilizando métricas como el error cuadrático medio o la precisión).
        Visualizar el árbol de decisión resultante (opcional, pero muy útil para entender cómo funciona el modelo).

    Construcción de un Random Forest:
        Entrenar un modelo de Random Forest utilizando Scikit-learn.
        Evaluar el rendimiento del modelo en el conjunto de prueba.
        Comparar el rendimiento del Random Forest con el del Árbol de Decisión.
        Realizar ajuste de hiperparámetros del Random Forest, para verificar si se puede mejorar el resultado.

    Análisis de Importancia de Características:
        Extraer la importancia de las características del modelo Random Forest.
        Visualizar las características más importantes para predecir la calidad del vino.
        Analizar los resultados.