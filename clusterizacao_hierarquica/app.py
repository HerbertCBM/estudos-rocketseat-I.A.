# Importar Libs
import pandas as pd
import streamlit as st
# Carregar dados e colocar no Cache do Streamlit (função com decorador)
@st.cache_data
def carregar_dados():
    return pd.read_csv('.\dataset\clusterizacao_laptops.csv')

# Criar DataFrame para carregar a função
df = carregar_dados()

# Sidebar para Filtro
st.sidebar.header('Filtros')

# Selecionar Modelos
model = st.sidebar.selectbox("Selecionar Modelo", df['model'])

# Filtrar modelo
df_laptop_modelo = df[df['model'] == model]

# Filtar cluster do modelo escolhido
df_laptop_final = df[df['cluster'] == df_laptop_modelo.iloc[0]['cluster']]

# Visualizar Modelos
st.write("Recomendação de Modelo")
st.table(df_laptop_final)