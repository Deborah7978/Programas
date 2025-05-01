# Con Pandas
import pandas as pd

# Crear un DataFrame de ejemplo
datos = {
 'Nombre': ['Deborah', 'Michael', 'Madeley', 'Lucía'],
 'Edad': [20, 23, 19, 21],
 'Ciudad': ['Santiago de Cuba', 'La Habana', 'Holguín', 'Camagüey']
}

df = pd.DataFrame(datos)

# Filtrar por edad mayor de 20
df_filtrado = df[df['Edad'] > 20]

# Agrupar por ciudad y contar
conteo_por_ciudad = df.groupby('Ciudad').count()

# Mostrar resultados
print("DataFrame original en Pandas:")
print(df)
print("\nDataFrame filtrado (edad > 20):")
print(df_filtrado)
print("\nConteo por ciudad:")
print(conteo_por_ciudad)


# Con Polars
import polars as pl

# Crear un DataFrame de ejemplo
df = pl.DataFrame(datos)

# Filtrar por edad mayor de 20
df_filtrado = df.filter(pl.col('Edad') > 20)

# Agrupar por ciudad y contar
conteo_por_ciudad = df.groupby('Ciudad').agg(pl.count())

# Mostrar resultados
print("DataFrame original en Polars:")
print(df)
print("\nDataFrame filtrado (edad > 20):")
print(df_filtrado)
print("\nConteo por ciudad:")
print(conteo_por_ciudad)
