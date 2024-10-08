import streamlit as st
import pandas as pd
#import numpy as np
import plotly.express as px
#import altair as alt


st.set_page_config(
    page_title="Dashboard Proyecto",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

# Crear un DataFrame de ejemplo
data = pd.read_csv('farmacias_departamento.csv')


# Título del Dashboard
st.title('Dashboard Famacias')

tabs = st.tabs(["Farmacias por Departamento", "Grafica 2", "Grafica 3"])

with tabs[0]: 
    # Filtros en la Barra Lateral
    st.sidebar.header('Filtros')
    filtro_departamento = st.sidebar.multiselect('Seleccione Departamento:', data['NOMBDEPTO'].unique())

    # Filtrar datos según selección
    df_filtrado = data.copy()

    if filtro_departamento:
        df_filtrado = df_filtrado[df_filtrado['NOMBDEPTO'].isin(filtro_departamento)]

    # Visualización 1: Gráfico de Farmacias por Departamento
    st.subheader('Farmacias por Departamento')
    fig1 = px.bar(df_filtrado, x='NOMBDEPTO', y='NOMDIR', title='Total de Farmacias por Departamento')
    st.plotly_chart(fig1)

with tabs[1]:
    # Filtros en la Barra Lateral
    st.sidebar.header('Filtros')
    filtro_departamento = st.sidebar.multiselect('Seleccione Departamento:', data['NOMBDEPTO'].unique())

    # Filtrar datos según selección
    df_filtrado = data.copy()

    if filtro_departamento:
        df_filtrado = df_filtrado[df_filtrado['NOMBDEPTO'].isin(filtro_departamento)]

    # Visualización 1: Gráfico de Farmacias por Departamento
    st.subheader('Farmacias por Departamento')
    fig1 = px.bar(df_filtrado, x='NOMBDEPTO', y='NOMDIR', title='Total de Farmacias por Departamento')
    st.plotly_chart(fig1)

with tabs[2]:
    # Filtros en la Barra Lateral
    st.sidebar.header('Filtros')
    filtro_departamento = st.sidebar.multiselect('Seleccione Departamento:', data['NOMBDEPTO'].unique())

    # Filtrar datos según selección
    df_filtrado = data.copy()

    if filtro_departamento:
        df_filtrado = df_filtrado[df_filtrado['NOMBDEPTO'].isin(filtro_departamento)]

    # Visualización 1: Gráfico de Farmacias por Departamento
    st.subheader('Farmacias por Departamento')
    fig1 = px.bar(df_filtrado, x='NOMBDEPTO', y='NOMDIR', title='Total de Farmacias por Departamento')
    st.plotly_chart(fig1)
