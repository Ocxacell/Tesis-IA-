import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier, Pool

# 1. Leer el archivo limpio
df = pd.read_excel("Datosrecorte_limpio.xlsx", sheet_name="Data")

# 2. Definir la variable target (ejemplo: 'Masivo', cámbiala si es otra)
target = "tiempo_solucion_horas"

# 3. Features = todas las demás columnas excepto target
X = df.drop(columns=[target])
y = df[target]

# 4. Dividir en train y test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Tamaño train:", X_train.shape)
print("Tamaño test:", X_test.shape)
