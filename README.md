# 📈 TFM: Predicción de Demanda y Optimización de Stock — Grupo Plásticos Ferro, S.L.

Este proyecto implementa el pipeline completo de **Ciencia de Datos** desarrollado para el Trabajo Fin de Máster (Máster en Matemática Industrial), en colaboración con Grupo Plásticos Ferro, S.L. El objetivo es predecir la demanda mensual agregada (variable `PESO_BRUTO`, en kg) de tres familias de producto con perfiles de demanda muy distintos, y usar esas predicciones como base para la optimización de inventario.

Familias analizadas:

- **106** — demanda intermitente / lumpy (muchos meses con valores próximos a cero).
- **124** — demanda heterocedástica, con varianza creciente en el tiempo.
- **233** — demanda regular, con tendencia suave.

Incluye:

- 🔄 Proceso ETL de extracción desde el ERP Oracle (vía SQL) y transformación a demanda mensual por familia
- 📊 Análisis exploratorio de datos (EDA), descomposición STL y estudio de estacionariedad
- 🤖 Modelado y comparación de métodos clásicos y de aprendizaje automático: Regresión Ridge, SARIMA, Prophet, XGBoost, LightGBM y LSTM (estándar y sobre log-diferencias)
- 🔍 Interpretabilidad mediante TreeSHAP (aplicado en exclusiva al modelo XGBoost)
- 📁 Generación de predicciones, métricas y figuras listas para su inclusión en la memoria del TFM (LaTeX)

---

## 📂 Estructura del Proyecto

```text
TFM/
├── data/
│   ├── raw/                        # Datos originales exportados del ERP
│   │   ├── Compras.xls
│   │   └── Ventas.xls
│   └── processed/                  # Datos y resultados generados por el pipeline
│       ├── datos.xlsx              # Dataset consolidado (demanda mensual por familia)
│       ├── 04_metricas_SARIMA_Prophet.csv
│       ├── 04_predicciones_test.csv
│       ├── 05_predicciones_ML.csv
│       ├── 06_metricas_global.csv
│       └── 06_metricas_logdiff.csv
├── figuras/                        # Gráficas generadas por los notebooks
├── figuras_latex/                  # Figuras exportadas en formato apto para la memoria LaTeX
├── notebooks/
│   ├── 01_EDA_PCA.ipynb            # Análisis exploratorio y PCA
│   ├── 02_Estacionariedad.ipynb    # Descomposición STL y tests de estacionariedad
│   ├── 03_Regression.ipynb         # Regresión Ridge (GridSearchCV + TimeSeriesSplit)
│   ├── 04_SARIMA_Prophet.ipynb     # Modelos SARIMA y Prophet
│   ├── 05_XGBoost_LightGBM.ipynb   # Modelos de árboles + interpretabilidad SHAP
│   ├── 06_a_LTSM.ipynb             # LSTM sobre la serie original
│   ├── 06_b_LTSM_logdiff.ipynb     # LSTM sobre la serie en log-diferencias
│   └── 07_Heatmap_Global.ipynb     # Comparativa global de métricas entre modelos y familias
├── src/                             # Código fuente modular
│   ├── __init__.py
│   └── etl.py                      # Lógica de extracción y limpieza de datos
├── venv/                           # Entorno virtual (NO subir a Git)
├── main.py                         # Script principal de ejecución del pipeline ETL
├── requirements.txt                # Dependencias del proyecto
└── .gitignore
```

---

# ⚙️ Requisitos Previos

Antes de empezar necesitas tener instalado:

- 🐍 Python 3.10 o superior (recomendado 3.11, por compatibilidad con Prophet y TensorFlow)
- 📦 pip (incluido con Python)

Comprobar versión:

```bash
python --version
```

---

# 🧪 Configuración del Entorno Virtual (venv)

## 1️⃣ Crear entorno virtual

Desde la raíz del proyecto:

```bash
python -m venv venv
```

## 2️⃣ Activar entorno virtual

### En Windows:

```bash
.\venv\Scripts\activate
```

Si no funciona:

```bash
venv\Scripts\activate.bat
```

### En Mac / Linux:

```bash
source venv/bin/activate
```

Cuando esté activo verás algo como:

```
(venv)
```

---

# 📦 Instalación de Dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

Si no existe el archivo aún, puedes instalar manualmente las dependencias principales:

```bash
pip install pandas numpy scikit-learn statsmodels prophet xgboost lightgbm tensorflow shap matplotlib seaborn openpyxl xlrd yfinance jupyter
```

---

## 📚 Librerías principales utilizadas

- `pandas` → Manipulación de series temporales y agregación mensual
- `numpy` → Operaciones numéricas
- `scikit-learn` → Regresión Ridge, escalado (`StandardScaler`), `TimeSeriesSplit`, métricas
- `statsmodels` → Descomposición STL, SARIMA / `auto_arima`, tests de estacionariedad
- `prophet` → Modelo Prophet
- `xgboost` / `lightgbm` → Modelos de gradient boosting
- `shap` → Interpretabilidad (TreeSHAP sobre XGBoost)
- `tensorflow` (Keras) → Modelos LSTM
- `yfinance` → Descarga de la serie de futuros de crudo WTI (`CL=F`), usada como variable exógena
- `matplotlib` / `seaborn` → Visualización
- `openpyxl` / `xlrd` → Lectura de archivos `.xlsx` / `.xls`
- `notebook` / `jupyterlab` → Entorno de desarrollo interactivo

---

# 📁 Archivos de Entrada

El proyecto espera encontrar los siguientes archivos en:

```
data/raw/
```

Archivos requeridos:

- `Compras.xls`
- `Ventas.xls`

⚠️ Los nombres deben coincidir exactamente (incluyendo mayúsculas y extensión) con los que utiliza `main.py` / `src/etl.py`.

El proceso ETL consolida estos archivos en:

```
data/processed/datos.xlsx
```

que es el dataset base consumido por todos los notebooks (columna `FAMILIA` como texto, alineada con las familias `['106', '124', '233']`, e índice temporal tipo `DatetimeIndex`).

---

# ▶️ Ejecución del Proyecto

## 1️⃣ Pipeline ETL

Desde la raíz del proyecto y con el entorno activado:

```bash
python main.py
```

Salida esperada:

```
--- Leyendo archivos de: data/raw/Compras.xls y data/raw/Ventas.xls ---
✅ Proceso completado. Archivo guardado en: data/processed/datos.xlsx
```

## 2️⃣ Notebooks de análisis y modelado

Una vez generado `datos.xlsx`, los notebooks deben ejecutarse en orden dentro de `notebooks/`:

1. `01_EDA_PCA.ipynb` — análisis exploratorio y componentes principales
2. `02_Estacionariedad.ipynb` — descomposición STL y tests de estacionariedad
3. `03_Regression.ipynb` — Regresión Ridge
4. `04_SARIMA_Prophet.ipynb` — SARIMA y Prophet
5. `05_XGBoost_LightGBM.ipynb` — modelos de árboles + SHAP
6. `06_a_LTSM.ipynb` y `06_b_LTSM_logdiff.ipynb` — modelos LSTM
7. `07_Heatmap_Global.ipynb` — comparativa final de métricas entre todos los modelos y familias

Cada notebook guarda sus resultados (predicciones, métricas y figuras) en `data/processed/` y `figuras/` / `figuras_latex/`, respectivamente.

---

# Uso de Jupyter Notebook

Para lanzar el entorno de notebooks:

```bash
jupyter notebook
```

O:

```bash
jupyter lab
```

Los notebooks se ejecutan y guardan dentro de:

```
notebooks/
```

---

# Generar requirements.txt

Si instalas nuevas librerías:

```bash
pip freeze > requirements.txt
```

---

# Preacuación: Problemas Comunes

## Error: No such file or directory

Verifica que los archivos originales estén en:

```
data/raw/
```

y que los nombres coincidan exactamente (`Compras.xls`, `Ventas.xls`, incluyendo mayúsculas y extensión).

---

## Error: `Import xlrd failed`

Instalar:

```bash
pip install xlrd
```

---

## Diferencia entre .xls y .xlsx

- `.xls` → requiere `xlrd`
- `.xlsx` → requiere `openpyxl`

---

## Error al ejecutar Prophet o TensorFlow

Estas librerías son sensibles a la versión de Python y del compilador de C++ instalado. Si falla la instalación, se recomienda usar Python 3.11 y, en Windows, tener instalado Microsoft C++ Build Tools.

---

# 🧹 Buenas Prácticas

- ❌ No subir `venv/` al repositorio
- ✅ Mantener actualizado `requirements.txt`
- ✅ Usar rutas relativas
- ✅ Separar lógica de ETL (`src/etl.py`) y notebooks de modelado
- ✅ Fijar semillas aleatorias (`random_state` / `seed`) en los modelos para reproducibilidad
- ✅ Ajustar `StandardScaler` y winsorización únicamente sobre el conjunto de entrenamiento, para evitar fuga de datos (data leakage)

---

# 🚀 Flujo del Proyecto

1. Extraer datos de compras y ventas desde el ERP (`data/raw/`)
2. Limpiar y transformar (ETL) → `data/processed/datos.xlsx`
3. Análisis exploratorio, PCA y estudio de estacionariedad (notebooks 01–02)
4. Entrenamiento y validación walk-forward de los modelos de predicción (notebooks 03–06), con los últimos 12 meses como conjunto de test
5. Comparación global de métricas entre modelos y familias (notebook 07)
6. Traslado de las predicciones a parámetros de gestión de inventario (stock de seguridad, punto de pedido, EOQ) en la memoria del TFM

---

# 👨‍💻 Autor

**Alexander** — Trabajo Fin de Máster, Máster en Matemática Industrial
Empresa colaboradora: Grupo Plásticos Ferro, S.L.
Tutor académico: Álvaro Leitao
Tutor industrial: José Antonio Fernández Iglesias (Departamento de IT)