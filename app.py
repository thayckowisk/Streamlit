import streamlit as st
import pandas as pd

st.set_page_config(page_title="Análise Exploratória")
st.title("Bem-vindo à Análise Exploratória das Despesas de Viagem")

# colocar os dados em cache
@st.cache_resource

def load_data():
    data = pd.read_csv("dados.csv", sep=";")
    data['PROPORCAO'] = data['VALOREMPENHO'] / data['PIB']
    return data

data = load_data()
st.session_state['data'] = data

with st.sidebar:
    st.header("Configurações Globais")
    if 'top_n' in st.session_state:
        default_top_n = st.session_state['top_n']
    else:
        default_top_n = 10

    top_n = st.number_input("Selecione o número de dados para exibir:",
                        min_value=1, max_value=len(data),
                        value=default_top_n)
    st.session_state['top_n'] = top_n