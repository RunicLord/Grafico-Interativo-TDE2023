import streamlit as st
import plots as p

st.set_page_config(page_title="Graficos")


option = st.sidebar.selectbox(
    'Gráficos',
    ('Assinantes netflix', 'Bilheteria', 'Publico cinema', 'Participação nacional',
     'Plano netflix VS Preço ingresso', 'Salário Mínimo VS Valor ingresso', 'Acesso a internet/domicílio',
     'Salas em funcionamento x Acesso a internet por domicílio'),
    index=None,
    placeholder='Escolha um gráfico...'
)

if option == 'Assinantes netflix':
    p.assinantes_netflix()
elif option == 'Bilheteria':
    p.bilheteria()
elif option == 'Publico cinema':
    p.publico_cinema()
elif option == 'Participação nacional':
    p.participacao_nacional()
elif option == 'Plano netflix VS Preço ingresso':
    p.plnetflix_x_ingresso()
elif option == 'Salário Mínimo VS Valor ingresso':
    p.salario_x_ingresso()
elif option == 'Acesso a internet/domicílio':
    p.domicilios_internet()
elif option == 'Salas em funcionamento x Acesso a internet por domicílio':
    p.salas_x_internet()
else:
    st.write('Nenhum gráfico selecionado')
