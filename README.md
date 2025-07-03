# Forecast Chilean Copper Exports 🇨🇱📈

Este repositorio contiene un proyecto de análisis y predicción de las exportaciones físicas de cobre chileno por tipo de producto (refinado, blíster y graneles), utilizando técnicas avanzadas de modelado de series de tiempo.

---

## 📌 Descripción

El objetivo principal es predecir mensualmente la cantidad de cobre exportado (en miles de toneladas métricas), utilizando datos históricos provistos por la Comisión Chilena del Cobre (COCHILCO) y el Servicio Nacional de Aduanas.

El proyecto abarca desde la exploración de los datos hasta la comparación de distintos modelos de forecasting, incluyendo:

- Prophet
- ARIMA
- Holt-Winters (Exponential Smoothing)
- XGBoost (con ingeniería de variables y lags)

Se realiza un análisis detallado sobre la serie de **exportaciones totales**, complementado por una comparación breve en los demás tipos de exportación.

---

## 📊 Origen de los datos

Los datos fueron obtenidos desde la página oficial de COCHILCO en el siguiente enlace:

👉 [Exportaciones de cobre por tipo de producto (Archivo Excel)](https://www.cochilco.cl:4040/boletin-web/pages/tabla20/buscar.jsf)

Estos archivos contienen información mensual desde 2003 en adelante, desglosada en:

- Cobre refinado
- Cobre blíster
- Cobre graneles
- Total exportado

---

## 🗂️ Estructura del repositorio

- `data/raw/` : Datos originales sin procesar (archivos Excel descargados).
- `data/processed/` : Datos limpios listos para análisis y modelado.
- `notebooks/` : Notebooks para limpieza, exploración y comparación de modelos.
- `src/` : Código fuente (funciones auxiliares, procesamiento y modelos).
- `README.md` : Documentación general del proyecto.

---

## 🛠️ Tecnologías y librerías usadas

- Python 3.10
- pandas, numpy, matplotlib, seaborn
- Prophet (Meta)
- statsmodels (ARIMA, Holt-Winters)
- xgboost, scikit-learn
- Jupyter Notebook

---

## 🚀 Instrucciones de uso

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/forecast-chilean-copper-exports.git```

2. Descarga el archivo Excel desde el sitio oficial de COCHILCO y guárdalo en data/raw/.

3. Ejecuta los notebooks en orden (empezando por exploración y limpieza).

4. Ajusta y entrena los modelos para comparar el rendimiento predictivo.

5. Revisa la tabla de métricas para elegir el mejor modelo.

---

## Referencias

- [Comisión Chilena del Cobre (COCHILCO)](https://www.cochilco.cl/)  
- [Servicio Nacional de Aduanas](https://www.aduanas.cl/)  

---