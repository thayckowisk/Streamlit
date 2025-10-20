import streamlit as st
import plotly.express as px

st.header("Distribuição dos Dados")

if 'data' not in st.session_state:
    st.error ("Dados não carregados!")
else:
    data = st.session_state['data']
    col1, col2 = st.columns(2)
    
    with col1:
        pict1 = px.histogram(data, x='VALOREMPENHO',
                             title='Histograma do Valor de Empenho')
        st.plotly_chart(pict1, use_container_width=True)

        pict2 = px.box(data, x='VALOREMPENHO',
                             title='BoxPlot do Valor de Empenho')
        st.plotly_chart(pict2, use_container_width=True)

    with col2:
        pict3 = px.histogram(data, x='PIB',
                             title='Histograma do PIB')
        st.plotly_chart(pict3, use_container_width=True)

        pict4 = px.box(data, x='PIB',
                             title='BoxPlot do PIB')
        st.plotly_chart(pict4, use_container_width=True)