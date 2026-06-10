import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Configuramos el título de la aplicación Streamlit
st.header("Analisis de anuncios de venta de coches")

# Cargamos el dataset de vehículos
car_data = pd.read_csv('vehicles_us.csv')

# Mostramos un texto introductorio para la sección de análisis exploratorio de datos
st.write("En esta sección se muestra un análisis exploratorio de los datos de anuncios de venta de coches. Se pueden construir gráficos interactivos para visualizar la distribución del odómetro y la relación entre el odómetro y el precio de los vehículos.")

# Creamos checkboxes para permitir al usuario elegir qué gráficos construir

build_histogram = st.checkbox(
    'Construir el histograma de la distribución del odómetro')
build_scatter = st.checkbox(
    'Construir el gráfico de dispersión para analizar la relación entre el odómetro y el precio')

# Si el usuario selecciona la opción para construir el histograma, se crea y muestra el histograma de la distribución del odómetro utilizando Plotly
if build_histogram:

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


# Si el usuario selecciona la opción para construir el gráfico de dispersión, se crea y muestra el gráfico de dispersión utilizando Plotly para analizar la relación entre el odómetro y el precio de los vehículos
if build_scatter:

    # Creamos un título para el scatter plot
    st.write("Grafico de dispersión para analizar la relación entre el odómetro y el precio de los vehículos")

    # Creamos el gráfico de dispersión utilizando la función pixel_scatter, que toma el DataFrame, las columnas para los ejes x e y, y un título para el gráfico
    fig = go.Figure(data=go.Scatter(
        x=car_data['odometer'], y=car_data['price'], mode='markers'))

    # Mostramos el gráfico de dispersión plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)


# ----- Este bloque de código se ha comentado para evitar que se ejecute la creación graficos atraves de botones en la aplicación Streamlit, pero se puede descomentar para mostrar los gráficos interactivos -----
# hist_button = st.button('Construir el histograma')
# scatter_button = st.button('Construir el gráfico de dispersión')

# if hist_button:
#
#    # Creamos un título para el histograma
#    st.write(
#        "Histograma de la distribución del odometro")
#
#    # Creamos el histograma utilizando Plotly
#    # Se crea una figura vacia y luego se añade un histograma con los odometros de los vehículos, especificando el número de bins
#    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'], nbinsx=50)])
#    fig.update_layout(title='Distribución de Odómetros',
#                      xaxis_title='Odómetro', yaxis_title='Frecuencia')
#
#    # Mostramos el histograma plotly interactivo en la aplicación Streamlit
#    # use_container_width=True hace que el gráfico ocupe todo el ancho disponible en la aplicación
#    st.plotly_chart(fig, use_container_width=True)

# if scatter_button:
#
#    # Creamos un título para el scatter plot
#    st.write("Grafico de dispersión para analizar la relación entre el odómetro y el precio de los vehículos")
#
#    # Creamos el gráfico de dispersión utilizando la función pixel_scatter, que toma el DataFrame, las columnas para los ejes x e y, y un título para el gráfico
#    fig = go.Figure(data=go.Scatter(
#        x=car_data['odometer'], y=car_data['price'], mode='markers'))
#
#    # Mostramos el gráfico de dispersión plotly interactivo en la aplicación Streamlit
#    st.plotly_chart(fig, use_container_width=True)
