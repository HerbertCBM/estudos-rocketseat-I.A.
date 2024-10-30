from fastapi import FastAPI # Construção da API
import uvicorn # Servidor para disponibilizar API
from pydantic import BaseModel # Forçar validação dos dados
import joblib # Carregar modelo
import pandas as pd # Criar df de predição

# Criar uma instância do FastAPI
app = FastAPI()

# Criar uma classe com os dados de entrada que 
# virão no request body com os tipos esperados

class request_body(BaseModel): # Tipo BaseModel: classe de validação de dados do pydantic
    tempo_na_empresa: int
    nivel_na_empresa: int

# Carregar modelo para realizar predição
modelo_poly = joblib.load('./modelo_salario.pkl')

# Função para fazer a predição
@app.post('/predict') # decorador da função: tipo rest.post + ./chamada
def predict(data: request_body): # Tipo do dado. O pydantic vai forçar os dados para virem no formato correto
    # Criando DF
    input_features = {
    'tempo_na_empresa': data.tempo_na_empresa,
    'nivel_na_empresa': data.nivel_na_empresa
    }

    pred_df = pd.DataFrame(input_features, index=[1])
    # Predição
    y_pred = modelo_poly.predict(pred_df)[0].astype(float) # Formatando o tipo do resultado 

    return {'salario_em_reais': y_pred.tolist()} # Para retornar corretamente é preciso converter a predição
                                                 # numa lista para o streamlit conseguir capturar corretamente

# Testar abrindo servidor uvicorn (Swager)