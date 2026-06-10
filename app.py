import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Cargamos el dataset de vehículos
car_data = pd.read_csv('vehicles_us.csv')


hist_button = st.button('Construir el histograma')
scatter_button = st.button('Construir el gráfico de dispersión')

if hist_button:

    # Creamos un título para el histograma
    st.write(
        "Histograma de la distribución del odometro")

    # Creamos el histograma utilizando Plotly
    # Se crea una figura vacia y luego se añade un histograma con los odometros de los vehículos, especificando el número de bins
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'], nbinsx=50)])
    fig.update_layout(title='Distribución de Odómetros',
                      xaxis_title='Odómetro', yaxis_title='Frecuencia')

    # Mostramos el histograma plotly interactivo en la aplicación Streamlit
    # use_container_width=True hace que el gráfico ocupe todo el ancho disponible en la aplicación
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:

    # Creamos un título para el scatter plot
    st.write("Grafico de dispersión para analizar la relación entre el odómetro y el precio de los vehículos")

    # Creamos el gráfico de dispersión utilizando la función pixel_scatter, que toma el DataFrame, las columnas para los ejes x e y, y un título para el gráfico
    fig = go.Figure(data=go.Scatter(
        x=car_data['odometer'], y=car_data['price'], mode='markers'))

    # Mostramos el gráfico de dispersión plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)
