import pandas as pd

# Leer desde la hoja "Data"
df = pd.read_excel("Datosrecorte.xlsx", sheet_name="Data")

# Convertimos a formato de fecha
df["Fecha/Hora de apertura"] = pd.to_datetime(df["Fecha/Hora de apertura"])
df["Fecha Solución"] = pd.to_datetime(df["Fecha Solución"])

# Calculamos la duración en horas
df["tiempo_solucion_horas"] = (df["Fecha Solución"] - df["Fecha/Hora de apertura"]).dt.total_seconds() / 3600

# 🚨 Eliminar registros con tiempo de solución negativo
df = df[df["tiempo_solucion_horas"] >= 0]

# Mostrar ejemplo
print("Dataset limpio, sin tiempos negativos ✅")
print(df[["Fecha/Hora de apertura", "Fecha Solución", "tiempo_solucion_horas"]].head(20))

# Guardar Excel limpio (opcional)
df.to_excel("Datosrecorte_limpio.xlsx", index=False, sheet_name="Data")
print("Archivo guardado como: Datosrecorte_limpio.xlsx")
