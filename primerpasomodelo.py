import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier, Pool
 
# 1. Leer el archivo limpio
df = pd.read_excel("Datosrecorte_limpio.xlsx", sheet_name="Data")
# Convertir la columna a tipo datetime (por si no lo está)
df["Fecha/Hora de apertura"] = pd.to_datetime(df["Fecha/Hora de apertura"], errors="coerce")

# Extraer características útiles de la fecha/hora

df["Mes_apertura"] = df["Fecha/Hora de apertura"].dt.month
df["Día_apertura"] = df["Fecha/Hora de apertura"].dt.day
df["Hora_apertura"] = df["Fecha/Hora de apertura"].dt.hour
df["Día_semana_apertura"] = df["Fecha/Hora de apertura"].dt.weekday  # 0=lunes, 6=domingo

# Eliminar la columna original (ya no se necesita como texto ni datetime)
df = df.drop(columns=["Fecha/Hora de apertura"])

# 2. Definir la variable target y columnas a ignorar(ejemplo: 'Masivo', cámbiala si es otra)
target = "tiempo_solucion_horas"
rows_to_ignore = ["Fecha_Solucion", target]  # Añade aquí las columnas que no quieres usar

# 3. Features = todas las demás columnas excepto target
X = df.drop(columns=rows_to_ignore)
y = df[target]

# Rellenar solo las columnas categóricas con "Desconocido"
cols_fillna = ["Segmentación IVR", "Masivo", "Segmento", "Subsegmento", "Municipio","Departamento"]
df[cols_fillna] = df[cols_fillna].fillna("Desconocido")

# Verificar que ya no hay nulos
print(df.isna().sum())

# 4. Dividir en train y test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Tamaño train:", X_train.shape)
print("Tamaño test:", X_test.shape)
print(X.head())   
print(y.head())   
# 1️⃣ Identificar columnas categóricas y numéricas
cat_features = X_train.select_dtypes(include=["object"]).columns.tolist()
num_features = X_train.select_dtypes(exclude=["object"]).columns.tolist()

print("Categorical features:", cat_features)
print("Numeric features:", num_features)
print(df.isnull().sum())