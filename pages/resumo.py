import streamlit as st

st.header("Resumo dos Dados")

if 'data' not in st.session_state:
    st.error ("Dados não carregados!")
else:
    data = st.session_state['data'].describe().reset_index()
    st.write(data)