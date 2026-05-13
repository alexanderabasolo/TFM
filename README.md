# 📈 TFM: Análisis de Datos y Pipeline de Predicción

Este proyecto implementa un flujo completo de **Ciencia de Datos** para la gestión de inventarios y ventas.

Incluye:

- 🔄 Proceso ETL (Extracción, Transformación y Carga)
- 📊 Análisis Exploratorio de Datos (EDA)
- 🤖 Preparación de Pipelines de Machine Learning
- 📁 Generación de dataset limpio listo para modelado

---

## 📂 Estructura del Proyecto

```text
TFM/
├── data/
│   ├── raw/                # Archivos Excel originales (compras.xls, ventas.xls)
│   └── processed/          # Datos limpios generados (analisis_final.xlsx)
├── notebooks/              # Jupyter Notebooks para EDA y visualizaciones
├── src/                    # Código fuente modular
│   ├── __init__.py
│   ├── etl.py              # Lógica de limpieza y transformación
│   └── model_logic.py      # Pipelines de Scikit-Learn
├── venv/                   # Entorno virtual (NO subir a Git)
├── main.py                 # Script principal de ejecución
├── requirements.txt        # Dependencias del proyecto
└── .gitignore
```

---

# ⚙️ Requisitos Previos

Antes de empezar necesitas tener instalado:

- 🐍 Python 3.10 o superior (recomendado 3.13)
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

Si no existe el archivo aún, puedes instalar manualmente:

```bash
pip install pandas scikit-learn matplotlib notebook openpyxl xlrd
```

---

## 📚 Librerías principales utilizadas

- `pandas` → Manipulación de datos
- `numpy` → Operaciones numéricas
- `scikit-learn` → Modelos de Machine Learning
- `matplotlib` → Visualización
- `notebook` / `jupyterlab` → EDA interactivo
- `openpyxl` → Lectura de archivos `.xlsx`
- `xlrd` → Lectura de archivos `.xls`
- `seaborn` → Gráficos
- `statsmodels`→ Estadística

---

# 📁 Archivos de Entrada

El proyecto espera encontrar los siguientes archivos en:

```
data/raw/
```

Archivos requeridos:

- `compras.xls`
- `ventas.xls`

⚠️ Si los archivos son `.xlsx`, asegúrate de que el nombre coincida exactamente con el que usa `main.py`.

---

# ▶️ Ejecución del Proyecto

Desde la raíz del proyecto y con el entorno activado:

```bash
python main.py
```

Salida esperada:

```
--- Leyendo archivos de: data/raw/compras.xls y data/raw/ventas.xls ---
✅ Proceso completado. Archivo guardado en: data/processed/analisis_final.xlsx
```

El archivo generado será:

```
data/processed/analisis_final.xlsx
```

---

# 📊 Uso de Jupyter Notebook (Opcional)

Para análisis exploratorio:

```bash
jupyter notebook
```

O:

```bash
jupyter lab
```

Los notebooks deben guardarse dentro de:

```
notebooks/
```

---

# 🛠️ Generar requirements.txt

Si instalas nuevas librerías:

```bash
pip freeze > requirements.txt
```

---

# ❗ Problemas Comunes

## Error: No such file or directory

Verifica que los archivos estén en:

```
data/raw/
```

Y que el nombre coincida exactamente (incluyendo extensión).

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

# 🧹 Buenas Prácticas

- ❌ No subir `venv/` al repositorio
- ✅ Mantener actualizado `requirements.txt`
- ✅ Usar rutas relativas
- ✅ Separar lógica ETL y modelado (implementado en `src/`)

---

# 🚀 Flujo del Proyecto

1. Leer datos Excel
2. Limpiar y transformar (ETL)
3. Unificar datasets
4. Guardar dataset final procesado
5. Preparar pipelines de modelado

---

# 👨‍💻 Autor

Trabajo Fin de Máster — Ciencia de Datos  
Proyecto de análisis y predicción de inventarios y ventas.