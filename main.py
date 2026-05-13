from src.etl import procesar_datos, guardar_resultado

def main():
    # Definimos las rutas de entrada
    PATH_COMPRAS = 'data/raw/Compras.xls'
    PATH_VENTAS = 'data/raw/Ventas.xls'
    
    try:
        # FASE 1: Procesamiento (ETL)
        datos_listos = procesar_datos(PATH_COMPRAS, PATH_VENTAS)
        
        # FASE 2: Guardado
        guardar_resultado(datos_listos, 'datos.xlsx')
        
        # Aquí podrías añadir: FASE 3: Predicción (Machine Learning)
        # entrenar_modelo(datos_listos)
        
    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")

if __name__ == "__main__":
    main()