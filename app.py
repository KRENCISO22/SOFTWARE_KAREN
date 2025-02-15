import pandas as pd
import plotly.express as px
import os
import streamlit as st

# Obtener el puerto desde la variable de entorno
PORT = int(os.environ.get("PORT", 8503))

st.set_page_config(page_title="Mi App en Render", page_icon="🚀")
st.write(f"La aplicación está corriendo en el puerto {PORT}")

car_data = pd.read_csv('C:/Users/krenc/SOFTWARE_KAREN/vehicles_us.csv') # leer los datos

# Título de la aplicación
st.title("Análisis de Datos de Vehículos")

# Vista previa de los datos
st.write("Vista previa del conjunto de datos:")
st.dataframe(car_data.head())

# Checkbox para mostrar histogramas
if st.checkbox("Mostrar Histograma del Odómetro"):
    st.write("Histograma del odómetro:")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig)

# Checkbox para mostrar gráfico de dispersión
if st.checkbox("Mostrar Gráfico de Dispersión (Precio vs. Año)"):
    st.write("Gráfico de dispersión del precio según el año del vehículo:")
    fig2 = px.scatter(car_data, x="model_year", y="price", title="Precio vs. Año del Vehículo")
    st.plotly_chart(fig2)
