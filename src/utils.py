import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.dates as mdates

def analisis_estacional(df, columna, titulo='', periodo=12):
    """
    Realiza un análisis de descomposición estacional y genera gráficos.
    
    Parámetros:
    -----------
    df : DataFrame
        DataFrame que contiene los datos
    columna : str
        Nombre de la columna a analizar
    titulo : str, opcional
        Título para los gráficos (si no se especifica, usará el nombre de la columna)
    periodo : int, opcional
        Periodo para la descomposición estacional (por defecto 12 para datos mensuales)
    """

    fecha_min = df['Fecha'].min()
    fecha_max = df['Fecha'].max()    
    if not titulo:
        titulo = columna

    # Descomposición estacional
    result = seasonal_decompose(df.set_index('Fecha')[columna], 
                              model='additive', 
                              period=periodo)

    fig, axes = plt.subplots(4, 1, figsize=(14, 10), sharex=True)
    components = {
        'Observado': result.observed,
        'Tendencia': result.trend,
        'Estacionalidad': result.seasonal,
        'Residuos': result.resid
    }

    for ax, (title, series) in zip(axes, components.items()):
        ax.plot(series)
        ax.set_title(title)
        
        ax.xaxis.set_major_locator(mdates.YearLocator())  # Marcas anuales
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))  # Formato mes/año
        ax.set_xlim(fecha_min, fecha_max)  # Forzar rango correcto
        
        ax.grid(True, linestyle='--', alpha=0.6)
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

    plt.tight_layout()
    fig.suptitle(f'Descomposición aditiva de {titulo} ({fecha_min.year}-{fecha_max.year})', 
                y=1.02, fontsize=14)
    plt.show()

    # Extraer el componente estacional
    estacionalidad = result.seasonal
    # Crear un DataFrame con mes y año por separado
    estacionalidad_df = estacionalidad.reset_index()
    estacionalidad_df['Mes'] = estacionalidad_df['Fecha'].dt.month
    estacionalidad_df['Año'] = estacionalidad_df['Fecha'].dt.year

    plt.figure(figsize=(14, 8))
    for year in estacionalidad_df['Año'].unique():
        year_data = estacionalidad_df[estacionalidad_df['Año'] == year]
        plt.plot(year_data['Mes'], year_data['seasonal'], 
                 label=year, alpha=0.7, marker='o')

    plt.title(f'Comparación Interanual de la Estacionalidad - {titulo}')
    plt.xlabel('Mes')
    plt.ylabel('Componente Estacional')
    plt.xticks(range(1, 13))
    plt.axhline(y=0, color='k', linestyle='--')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.show()
    