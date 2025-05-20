
# Previsão de Área Irrigada por Regressão Linear

Este projeto utiliza regressão linear simples para prever a área irrigada por ângulo com base nas horas de irrigação. É um exemplo didático para ilustrar como modelos lineares podem ser usados para suporte à decisão em operações agrícolas.

## Objetivo

Prever a área irrigada por ângulo a partir do número de horas de irrigação, permitindo:

- Melhor planejamento de uso de recursos (tempo, água, energia)
- Estimativas de cobertura para diferentes durações de irrigação

## Estrutura

- `regr_linear_irrigacao.ipynb` – notebook completo com EDA, modelagem, avaliação e predições.
- Gráficos e análises visuais para explicar cada etapa.

## Etapas do Projeto

1. **Carregamento dos Dados**  
   Dataset com variáveis numéricas representando horas e área irrigada.

2. **Análise Exploratória (EDA)**  
   Relação perfeitamente linear identificada entre as variáveis.

3. **Modelagem**  
   - Regressão Linear Simples
   - Avaliação com MAE e MSE próximos de zero
   - Análise de resíduos confirmando ajuste perfeito

4. **Predições de Exemplo**  
   - Ex: 15 horas → previsão de 1000 m² irrigados

## Resultados

- Equação da reta: `Área = 0.01 * Horas`
- MAE: 0.00 | MSE: 0.00
- Modelo altamente eficaz nos dados simulados

## Conclusão

O modelo mostra que é possível prever com alta precisão a área irrigada por tempo. Porém, para uso em campo, recomenda-se incorporar variabilidade real (tipo de solo, clima, etc).

## Aprendizados

- A importância de explorar visualmente os dados antes de modelar
- Como interpretar resíduos e métricas
- Como transformar previsões técnicas em decisões operacionais

## Requisitos

- Python 3.8+
- Bibliotecas: `pandas`, `matplotlib`, `seaborn`, `scikit-learn`

## Autor

Herbert Carvalho (com mentoria analítica via ChatGPT)
