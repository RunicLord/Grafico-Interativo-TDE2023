import streamlit as st

A, F, L = st.tabs(["Amanda", "Felipe", "Lucas"])

with A:
    st.subheader("Amanda Naraoka")
    st.write("Currículo Lattes: https://lattes.cnpq.br/0985159531653864")
with F:
    st.subheader("Felipe de Abreu Viljoen")
    st.write("Currículo Lattes: http://lattes.cnpq.br/2941232279485017")

with L:
    st.subheader("Lucas Vinicius Dimarzio Carneiro")
    st.write("Currículo Lattes: http://lattes.cnpq.br/5695976297861259")
