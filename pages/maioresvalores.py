import streamlit as st
import plotly.express as px

st.header("Maiores Valores")

if 'data' not in st.session_state:
    st.error ("Dados não carregados!")
else:
    top_n = st.session_state.get('top_n', 10)
    data = st.session_state['data']

    col1, col2, col3 = st.columns(3)

    with col1:
        Meffort = data.nlargest(top_n, 'VALOREMPENHO')
        pict1 = px.bar(Meffort, x='MUNICIPIO', y='VALOREMPENHO',
                      title='Maiores Empenhos')
        st.plotly_chart(pict1, use_container_width=True)

    with col2:
        Mpibs = data.nlargest(top_n, 'PIB')
        pict2 = px.pie(Mpibs, values='PIB', names='MUNICIPIO',
                      title='Maiores PIBs')
        st.plotly_chart(pict2, use_container_width=True)

    with col3:
        Mprop = data.nlargest(top_n, 'PROPORCAO')
        pict3 = px.bar(Mprop, x='MUNICIPIO', y='PROPORCAO',
                      title='Maiores Gastos em Proporção ao PIB')
        st.plotly_chart(pict3, use_container_width=True)        