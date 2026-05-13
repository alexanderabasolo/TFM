import pandas as pd
import os

def procesar_datos(ruta_compras, ruta_ventas):
    print(f"--- Iniciando Ingesta de Datos ---")
    
    # 1. Leer archivos con el motor xlrd
    df_compras = pd.read_excel(ruta_compras, engine='xlrd')
    df_ventas = pd.read_excel(ruta_ventas, engine='xlrd')
    
    # 2. Etiquetar el origen
    df_compras['TIPO_OPERACION'] = 'COMPRA'
    df_ventas['TIPO_OPERACION'] = 'VENTA'
    
    # 3. Normalizar nombres de columnas
    df_compras = df_compras.rename(columns={
        'CODIGO_PROVEEDOR': 'ID_ENTIDAD',
        'CODIGO_ART_': 'ID_ARTICULO', 
        'CODIGO_ARTICULO': 'ID_ARTICULO'
    })
    
    df_ventas = df_ventas.rename(columns={
        'CLIENTE': 'ID_ENTIDAD',
        'ARTICULO': 'ID_ARTICULO'
    })
    
    # 4. Unir los datos
    df_final = pd.concat([df_compras, df_ventas], ignore_index=True)

    # --- CAMBIO EXACTO AQUÍ: LIMPIEZA DE VALORES 0 Y NEGATIVOS ---
    total_antes = len(df_final)
    # Filtramos: PESO_BRUTO (kilos) > 0 e IMPORTE_NETO (euros) > 0
    df_final = df_final[(df_final['PESO_BRUTO'] > 0) & (df_final['IMPORTE_NETO'] > 0)]
    eliminados = total_antes - len(df_final)
    print(f"🧹 Limpieza: Se eliminaron {eliminados} registros con valores <= 0 en kilos o euros.")
    # -------------------------------------------------------------
    
    # 5. TRATAMIENTO DE FECHAS
    df_final['FECHA'] = pd.to_datetime(df_final['FECHA'], errors='coerce')
    df_final = df_final.dropna(subset=['FECHA'])

    # --- NUEVA SECCIÓN: INGENIERÍA DE CARACTERÍSTICAS ---
    # 5.1. Extraer información temporal (Clave para Predicción)
    df_final['AÑO'] = df_final['FECHA'].dt.year
    df_final['MES'] = df_final['FECHA'].dt.month
    df_final['DIA_SEMANA'] = df_final['FECHA'].dt.dayofweek # 0=Lunes, 6=Domingo
    df_final['TRIMESTRE'] = df_final['FECHA'].dt.quarter
    df_final['ES_FIN_DE_SEMANA'] = df_final['DIA_SEMANA'].isin([5, 6]).astype(int)
    # ----------------------------------------------------
    
    # 6. Limpieza de columnas vacías
    df_final.columns = df_final.columns.str.strip()
    
    return df_final

def guardar_resultado(df, nombre_archivo):
    os.makedirs('data/processed', exist_ok=True)
    ruta_final = os.path.join('data/processed', nombre_archivo)
    df.to_excel(ruta_final, index=False)
    print(f"✅ Éxito: {len(df)} registros procesados y enriquecidos.")