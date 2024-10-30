# Construindo Frontend da Aplicação
import streamlit as st # Construtor FrontEnd
import json # Converter e Receber os dados que serão inseridos na API
import requests # Faz chamadas da API

# Titulo da Aplicação
st.title("Modelo de Predição de Salário")

# Inputs do Usuário
# Celula para preenchimento da Variável 'tempo_na_empresa'
st.write("Quantos meses o profissional está na empresa?")
tempo_na_empresa = st.slider("Meses", min_value=1, max_value=120, value=60, step=1)

# Celula para preenchimento da Variável 'nivel_na_empresa'
st.write("Qual o nível do profissional na empresa?")
nivel_na_empresa = st.slider("Nível", min_value=1, max_value=10, value=5, step=1)



# Preparar dados para API
input_features = {'tempo_na_empresa': tempo_na_empresa,
                  'nivel_na_empresa': nivel_na_empresa
                  }

# Criar um botão e capturar um evento para disparar a API
if st.button('Estimar Salário'):
    # Ação para chamar a API
    res = requests.post(url = 'http://127.0.0.1:8000/predict', 
                        json=input_features # Convertendo features para entrada no request
                        ) # Modulo que aciona a API
    
    # Filtrando o retorno que converte o json para trazer o output que queremos
    ret_json = json.loads(res.text)
    # Criando o indice do retorno da aplicação
    salario_em_reais = round(ret_json['salario_em_reais'], 2)
    # Mostrando a informação como subheader
    st.subheader(f'O salário estimado é de R${salario_em_reais}')

    