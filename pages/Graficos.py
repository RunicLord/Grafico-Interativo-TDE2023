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
    st.divider()
elif option == 'Bilheteria':
    p.bilheteria()
    st.divider()
elif option == 'Publico cinema':
    p.publico_cinema()
    st.divider()
elif option == 'Participação nacional':
    p.participacao_nacional()
    st.divider()
elif option == 'Plano netflix VS Preço ingresso':
    p.plnetflix_x_ingresso()
    st.divider()
elif option == 'Salário Mínimo VS Valor ingresso':
    p.salario_x_ingresso()
    st.divider()
elif option == 'Acesso a internet/domicílio':
    p.domicilios_internet()
    st.divider()
elif option == 'Salas em funcionamento x Acesso a internet por domicílio':
    p.salas_x_internet()
    st.divider()
else:
    st.sidebar.success('Escolha um gráfico acima')
    st.write('Nenhum gráfico selecionado')
    st.caption("""
    Você pode resetar o zoom do grafico clicando duas vezes com o botão esquerdo do mouse  
    Você também pode trocar as ferramentas de zoom e mover no menu localizado no canto superior direito do gráfico  

    Para visualizar um gráfico, basta selecionar no seletor na barra lateral.
    """)
