# Dashboard de Anúncios de Venda de Carros

Este aplicativo tem como finalidade mostrar, de forma simples e objetiva, anúncios de venda de carros por meio de gráficos. O conjunto de dados faz parte do projeto do curso de Análise de Dados da TripleTen (Sprint 5).

## Acesse o aplicativo

[projeto_tripletensprint5](https://projeto-tripletensprint5.onrender.com/)

> Nota: o app está no plano gratuito do Render. Depois de um período sem
> acessos, a primeira visita pode demorar vários minutos. Se necessário,
> recarregue a página algumas vezes.

## O que o aplicativo faz

- **Histograma**: cria um histograma interativo da quilometragem (`odometer`), com as barras coloridas pela condição do veículo (`condition`).
- **Gráfico de dispersão**: relaciona a quilometragem (`odometer`) ao preço (`price`), e as cores mostram a condição do veículo (`condition`).
- **Histograma por coluna**: o usuário escolhe uma coluna (`model_year`, `odometer`, `price`, `days_listed` ou `type`) e o histograma é redesenhado, também colorido por `condition`.

## Dados

Arquivo: `vehicles_us.csv`, com 51.525 anúncios de venda de carros. As colunas `price`, `odometer` e `condition` têm mais destaque no aplicativo, por serem fatores que muitos compradores observam com atenção.

## Tecnologias

Python, pandas, Plotly Express, Streamlit e Render.

## Como rodar localmente

Com o conda instalado:

```bash
conda create -n vehicles_env python=3.12
conda activate vehicles_env
pip install -r requirements.txt
streamlit run app.py
```

Por causa do arquivo `.streamlit/config.toml`, o aplicativo abre em `http://localhost:10000` (e não na porta padrão, 8501). O navegador não abre sozinho: acesse esse endereço manualmente.

## Estrutura do repositório

```
.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── notebooks/
│   └── EDA.ipynb
└── .streamlit/
    └── config.toml
```