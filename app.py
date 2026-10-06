import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.title('Visualização de Dados de Anúncios de Carros')
st.header('Anúncios de venda de carros')
st.write('Este aplicativo permite que você visualize dados de anúncios de venda de carros.')
