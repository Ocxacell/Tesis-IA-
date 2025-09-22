import pandas as pd

# Leer desde la hoja "Data"
df = pd.read_excel("Datosrecorte.xlsx", sheet_name="Data")

# Configurar pandas para mostrar TODO
pd.set_option("display.max_columns", None) # Todas las columnas

print(df.head(10))  # Muestra las primeras 10 filas pero con TODAS las columnas

# Convertimos a formato de fecha
df["Fecha/Hora de apertura"] = pd.to_datetime(df["Fecha/Hora de apertura"])
df["Fecha Solución"] = pd.to_datetime(df["Fecha Solución"])

# Calculamos la duración en horas
df["tiempo_solucion_horas"] = (df["Fecha Solución"] - df["Fecha/Hora de apertura"]).dt.total_seconds() / 3600


print(df[["Fecha/Hora de apertura", "Fecha Solución", "tiempo_solucion_horas"]].head(100))
# Filtrar filas con tiempo de solución negativo
negativos = df[df["tiempo_solucion_horas"] < 0]

# Contar cuántos casos hay
print("Número de casos con tiempo de solución negativo:", len(negativos))

# Si quieres ver algunos ejemplos:
print(negativos[["Fecha/Hora de apertura", "Fecha Solución", "tiempo_solucion_horas"]].head(10))
