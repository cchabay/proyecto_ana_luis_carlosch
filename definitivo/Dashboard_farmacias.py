import streamlit as st
import pandas as pd
import plotly.express as px
#import folium #Librería de mapas en Python
from streamlit_folium import st_folium #Widget de Streamlit para mostrar los mapas
#from folium.plugins import MarkerCluster #Plugin para agrupar marcadores


st.set_page_config(
    page_title="Dashboard Proyecto",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded")

# Crea dataframe de farmacias por departamento
df_farmacias_depto = pd.read_csv('farmacias_departamento.csv')

# Crea dataframe de todas las farmacias de Uruguay
df_farmacias = pd.read_csv('farmacias_loc_depto.csv')

# Crea dataframe loc grandes sin farmacias
df_loc_grandes_sin_farm = pd.read_csv('loc_grandes_sin_farm.csv')

# Crea dataframe loc chicas con farmacias
df_loc_chicas_con_farm = pd.read_csv('loc_chicas_con_farm.csv')

# Título del Dashboard
st.title('INE - Dashboard Famacias')
st.logo('logoINE_Transparente.png',size="large", link=None, icon_image=None)

#tabs = st.tabs(["Total de Farmacias por Departamento", "Ubicación de Farmacias", "Grafica 3"])
tab1,tab2,tab3=st.tabs(["Total de Farmacias por Departamento",
                        "Ubicación de Farmacias",
                        "Localidades con cantidad de farmacias atípicas"])

# Filtros en la Barra Lateral
st.sidebar.header('Filtros')
filtro_departamento = st.sidebar.multiselect('Seleccione Departamento:', df_farmacias_depto['NOMBDEPTO'].unique())

with tab1: 
    # Filtrar datos según selección
    df_filtrado = df_farmacias_depto.copy()

    if filtro_departamento:
        df_filtrado = df_filtrado[df_filtrado['NOMBDEPTO'].isin(filtro_departamento)]

    # Visualización 1: Gráfico de Farmacias por Departamento
    st.subheader('Farmacias por Departamento')
    fig1 = px.bar(df_filtrado, x='NOMBDEPTO', y='CANT_FARMACIAS', title='Total de Farmacias por Departamento')
    st.plotly_chart(fig1)

with tab2:
    # tab2

# Filtros en la Barra Lateral
    #st.sidebar.header('Filtros')
    #filtro_departamento = st.sidebar.multiselect('Seleccione Departamento:', df_Farmacias['NOMBDEPTO'].unique())   
    filtro_nombre_farmacia = st.text_input('Nombre de Farmacia: ')
    # Filtrar datos según selección
    #df_filtrado = df_farmacias_depto.copy()

    if filtro_nombre_farmacia:
        #df_farmacias = df_farmacias[df_farmacias['NOMBRE'].isin(filtro_nombre_farmacia)]
        df_farmacias = df_farmacias[df_farmacias['NOMBRE'].str.contains(filtro_nombre_farmacia, case=False)]

    if filtro_departamento:
        df_farmacias = df_farmacias[df_farmacias['NOMDEPTO'].isin(filtro_departamento)]

    #st.sidebar.header('Filtros')
    #parMapa = st.selectbox('Tipo Mapa',options=["open-street-map", "carto-positron","carto-darkmatter"])        
    #parTamano = st.checkbox('Tamaño por cantidad de reviews')
    fig = px.scatter_mapbox(df_farmacias,lat='LATITUD',lon='LONGITUD', 
                                hover_name='NOMBRE',hover_data=['DIRECCION','NOMBLOC', 'NOMDEPTO'],
                                zoom=5, height=600)
    fig.update_layout(mapbox_style='open-street-map')
    st.plotly_chart(fig,use_container_width=True)


with tab3:
    st.subheader('Localidades con cantidad de farmacias atípicas')
    cuadro = st.radio('Cuadro:',options=['Localidades de mas de 3.000 habitantes sin farmacias en un radio de 1 km',
                                         'Localidades de menos de 3.000 habitantes con farmacias en un radio de 1 km'],horizontal=False)
    if cuadro == 'Localidades de mas de 3.000 habitantes sin farmacias en un radio de 1 km':
        if filtro_departamento:
            df_loc_grandes_sin_farm = df_loc_grandes_sin_farm[df_loc_grandes_sin_farm['NOMBDEPTO'].isin(filtro_departamento)]

        st.dataframe(df_loc_grandes_sin_farm, use_container_width=True)

    else:
        if filtro_departamento:
            df_loc_chicas_con_farm = df_loc_chicas_con_farm[df_loc_chicas_con_farm['NOMBDEPTO'].isin(filtro_departamento)]

        st.dataframe(df_loc_chicas_con_farm, use_container_width=True)