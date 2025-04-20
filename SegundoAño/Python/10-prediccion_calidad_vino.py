import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv('vino_calidad.csv')

print(df.head())
print(df.describe())


#Variable Objetivo: Calidad
sns.countplot(x='calidad', data=df)
plt.title('Distribución de la Calidad del Vino')
plt.show()

sns.boxplot(x='calidad', y='alcohol', data=df)
plt.title('Relación entre Alcohol y Calidad')
plt.show()
   
#Conjunto de Datos: Características y variable objetivo
X = df.drop('calidad', axis=1) 
y = df['calidad']     

#Conjunto: Entrenamiento y Prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

escalador = StandardScaler()
X_entrenamiento = escalador.fit_transform(X_entrenamiento)
X_prueba = escalador.transform(X_prueba)
   
#Construcción de un Árbol de Decisión
arbol_decision = DecisionTreeRegressor(random_state=42)
arbol_decision.fit(X_entrenamiento, y_entrenamiento)

y_pred_arbol = arbol_decision.predict(X_prueba)
mse_arbol = mean_squared_error(y_prueba, y_pred_arbol)
print(f'Error Cuadrático Medio del Árbol de Decisión: {mse_arbol}')

#Construcción de un Random Forest
random_forest = RandomForestRegressor(random_state=42)
random_forest.fit(X_entrenamiento, y_entrenamiento)

y_pred_rf = random_forest.predict(X_prueba)
mse_rf = mean_squared_error(y_prueba, y_pred_rf)
print(f'Error Cuadrático Medio del Random Forest: {mse_rf}')

#Comparación: Árbol de Decisión y Random Forest
print(f'Comparación de MSE:\nÁrbol de Decisión: {mse_arbol}\nRandom Forest: {mse_rf}')

#Ánalisis de Importancia de Características
importancias = random_forest.feature_importances_
nombres_caracteristicas = X.columns
df_importancia = pd.DataFrame({'Característica': nombres_caracteristicas, 'Importancia': importancias})
df_importancia = df_importancia.sort_values(by='Importancia', ascending=False)
print(df_importancia)

sns.barplot(x='Importancia', y='Característica', data=df_importancia.head(10))
plt.title('Características más Importantes')
plt.show()