# Dashboard de Preço do Carbono - Reino Unido

## Descrição

Este dashboard foi desenvolvido usando Flask com arquitetura 5C para analisar a evolução do preço do carbono no Reino Unido entre 2010-2020 e fazer predições para 2020-2030.

## Arquitetura 5C Implementada

- **Controller**: Rotas Flask (`src/routes/dashboard.py`)
- **Configuration**: Configurações da aplicação (`src/config/config.py`)
- **Component**: Modelos de dados (`src/models/carbon_data.py`)
- **Core**: Serviços de negócio (`src/services/carbon_service.py`)
- **Common**: Utilitários e recursos compartilhados

## Funcionalidades

- **Análise Histórica**: Visualização dos dados de preço do carbono de 2010-2020
- **Predições**: Projeções para 2021-2030 usando modelo de regressão linear
- **Estatísticas**: Métricas comparativas entre as duas décadas
- **Visualizações Interativas**: Gráficos usando Plotly.js
- **Interface Responsiva**: Design adaptável para desktop e mobile

## Como Executar

### 1. Navegue até o diretório do projeto
```bash
cd carbon_dashboard
```

### 2. Ative o ambiente virtual
```bash
source venv/bin/activate
```

### 3. Execute a aplicação
```bash
python src/main.py
```

### 4. Acesse o dashboard
Abra seu navegador e vá para: `http://localhost:5000`

## Estrutura do Projeto

```
carbon_dashboard/
├── src/
│   ├── config/
│   │   └── config.py          # Configurações da aplicação
│   ├── models/
│   │   ├── carbon_data.py     # Modelo de dados do carbono
│   │   └── user.py           # Modelo de usuário (template)
│   ├── routes/
│   │   ├── dashboard.py       # Rotas do dashboard
│   │   └── user.py           # Rotas de usuário (template)
│   ├── services/
│   │   └── carbon_service.py  # Serviços de processamento de dados
│   ├── static/
│   │   └── index.html        # Interface do dashboard
│   ├── database/
│   │   └── app.db           # Banco de dados SQLite
│   ├── carbon_price_uk_2010-2020_processed.csv
│   ├── carbon_price_uk_2021-2030_predictions.csv
│   └── main.py              # Ponto de entrada da aplicação
├── venv/                    # Ambiente virtual Python
└── requirements.txt         # Dependências do projeto
```

## APIs Disponíveis

- `GET /api/dashboard/data` - Retorna todos os dados (históricos e predições)
- `GET /api/dashboard/charts/line` - Retorna gráfico de evolução temporal
- `GET /api/dashboard/charts/comparison` - Retorna gráfico de comparação entre décadas
- `GET /api/dashboard/statistics` - Retorna estatísticas dos dados

## Tecnologias Utilizadas

- **Backend**: Flask, Python 3.11
- **Frontend**: HTML5, CSS3, JavaScript, Plotly.js
- **Dados**: Pandas, Scikit-learn
- **Banco de Dados**: SQLite
- **Visualização**: Plotly

## Insights dos Dados

- **Preço Médio Histórico (2010-2020)**: €12.05
- **Preço Médio Predito (2021-2030)**: €25.95
- **Taxa de Crescimento**: 115.3%
- **Preço Máximo Histórico**: €27.08

O modelo prevê um crescimento significativo no preço do carbono na próxima década, refletindo as políticas ambientais mais rigorosas e a crescente demanda por créditos de carbono.

## Observações

- O modelo de predição utiliza regressão linear simples baseada na tendência histórica
- Para predições mais precisas, considere usar modelos mais sofisticados como ARIMA ou LSTM
- Os dados são baseados no sistema ETS (Emissions Trading System) do Reino Unido

