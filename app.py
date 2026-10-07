import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.title('Visualização de Dados de Anúncios de Carros')
st.header('Anúncios de venda de carros')
st.write('Este aplicativo permite que você visualize dados de anúncios de venda de carros.')

hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer", color="condition")
    st.plotly_chart(fig, width='stretch')

if st.button('Criar gráfico de dispersão'):
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x="odometer", y="price", color="condition")
    st.plotly_chart(fig, width='stretch')

st.subheader('Histograma por coluna')
coluna = st.selectbox(
    'Escolha a coluna para o eixo x',
    ['model_year', 'odometer', 'price', 'days_listed', 'type'],
)
fig = px.histogram(car_data, x=coluna, color='condition',
                   title=f'Histograma de {coluna} por condição')
st.plotly_chart(fig, width='stretch')