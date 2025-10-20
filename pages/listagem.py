import streamlit as st
from st_aggrid import AgGrid

st.header("Visualização de Dados")

if 'data' not in st.session_state:
    st.error ("Dados não carregados!")
else:
    top_n = st.session_state.get('top_n', 10)
    data = st.session_state['data']
    data_filtered = data.head(top_n)
    AgGrid(data_filtered, fit_columns_on_grid_load=True)