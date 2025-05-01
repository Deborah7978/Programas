# Con Pandas
import pandas as pd

# Crear un DataFrame de ejemplo
datos = {
 'Nombre': ['Alice', 'Bob', 'Charlie', 'David'],
 'Edad': [24, 27, 22, 32],
 'Ciudad': ['Nueva York', 'Los Ángeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(datos)

# Filtrar por edad mayor de 25
df_filtrado = df[df['Edad'] > 25]

# Agrupar por ciudad y contar
conteo_por_ciudad = df.groupby('Ciudad').count()

# Mostrar resultados
print("DataFrame original en Pandas:")
print(df)
print("\nDataFrame filtrado (edad > 25):")
print(df_filtrado)
print("\nConteo por ciudad:")
print(conteo_por_ciudad)


# Con Polars
import polars as pl

# Crear un DataFrame de ejemplo
df = pl.DataFrame(datos)

# Filtrar por edad mayor de 25
df_filtrado = df.filter(pl.col('Edad') > 25)

# Agrupar por ciudad y contar
conteo_por_ciudad = df.groupby('Ciudad').agg(pl.count())

# Mostrar resultados
print("DataFrame original en Polars:")
print(df)
print("\nDataFrame filtrado (edad > 25):")
print(df_filtrado)
print("\nConteo por ciudad:")
print(conteo_por_ciudad)