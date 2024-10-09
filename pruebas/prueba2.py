import streamlit as st
import pandas as pd
import plotly.express as px
import folium #Librería de mapas en Python
from streamlit_folium import st_folium #Widget de Streamlit para mostrar los mapas
from folium.plugins import MarkerCluster #Plugin para agrupar marcadores


st.set_page_config(
    page_title="Dashboard Proyecto",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

# Crea dataframe de farmacias por departamento
data_tab0 = pd.read_csv('farmacias_departamento.csv')

# Crea dataframe de todas las farmacias de Uruguay
df_farmacias = pd.read_csv('farmacias_loc_depto.csv')


# Título del Dashboard
st.title('Dashboard Famacias')

tabs = st.tabs(["Total de Farmacias por Departamento", "Ubicación de Farmacias", "Grafica 3"])

with tabs[0]: 
    # Filtros en la Barra Lateral
    st.sidebar.header('Filtros')
    filtro_departamento = st.sidebar.multiselect('Seleccione Departamento:', data_tab0['NOMBDEPTO'].unique())

    # Filtrar datos según selección
    df_filtrado = data_tab0.copy()

    if filtro_departamento:
        df_filtrado = df_filtrado[df_filtrado['NOMBDEPTO'].isin(filtro_departamento)]

    # Visualización 1: Gráfico de Farmacias por Departamento
    st.subheader('Total de Farmacias por Departamento')
    fig1 = px.bar(df_filtrado, x='NOMBDEPTO', y='CANT_FARMACIAS', title='Total de Farmacias por Departamento')
    st.plotly_chart(fig1)

with tabs[1]:
    # tab1

# Filtros en la Barra Lateral
    #st.sidebar.header('Filtros')
    #filtro_departamento = st.sidebar.multiselect('Seleccione Departamento:', df_Farmacias['NOMBDEPTO'].unique())

    # Filtrar datos según selección
    #df_filtrado = data_tab0.copy()

    #if filtro_departamento:
    #    df_Farmacias = df_Farmacias[df_Farmacias['NOMBDEPTO'].isin(filtro_departamento)]


    #st.sidebar.header('Filtros')
    #parMapa = st.selectbox('Tipo Mapa',options=["open-street-map", "carto-positron","carto-darkmatter"])        
    #parTamano = st.checkbox('Tamaño por cantidad de reviews')
    fig = px.scatter_mapbox(df_farmacias,lat='latitud',lon='longitud', 
                                hover_name='NOMBRE',hover_data=['DIRECCION','nombloc', 'NOMDEPTO'],
                                zoom=10, height=600)
    fig.update_layout(mapbox_style='open-street-map')
    st.plotly_chart(fig,use_container_width=True)


with tabs[2]:
    # tab2
    st.sidebar.header('Filtros')
