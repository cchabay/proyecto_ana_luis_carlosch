### **Ejercicio 1: Dashboard Interactivo Simple**

#Utilizando el dataset proporcionado (`dashboard_simple_data.csv`), crea un dashboard interactivo con los siguientes elementos:

#1. **Título y Subtítulo**: Añade un título claro y un subtítulo descriptivo.
#2. **Filtro Básico**: Utiliza un filtro para seleccionar una de las categorías (A, B o C).
#3. **Visualización Básica**: Muestra una visualización básica (como un gráfico de barras) que muestre el total de valores por fecha para la categoría seleccionada.


import streamlit as st
import pandas as pd
#import numpy as np
import plotly.express as px
#import altair as alt


st.set_page_config(
    page_title="Dashboard ejercicio 1",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

# Crear un DataFrame de ejemplo
data = pd.read_csv('dashboard_simple_data.csv')


# Título del Dashboard
st.title('Dashboard simple')

# Filtros en la Barra Lateral
st.sidebar.header('Filtros')
filtro_categoria = st.sidebar.multiselect('Selecciona Categoría:', data['Categoria'].unique())

# Filtrar datos según selección
df_filtrado = data.copy()

if filtro_categoria:
    df_filtrado = df_filtrado[df_filtrado['Categoria'].isin(filtro_categoria)]

# Visualización 1: Gráfico de Barras de Ventas por Producto
st.subheader('Valores por Fecha')
fig1 = px.bar(df_filtrado, x='Fecha', y='Valor', color='Categoria', title='Total de Valores por Fecha')
st.plotly_chart(fig1)