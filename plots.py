import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st

pd.options.plotting.backend = "plotly"

# ______Dataset Netflix_________________________________________________________________________________________
df = pd.read_csv("Datasets/2019-2017.csv", sep=';')
df = df.fillna("")
df = df.drop(columns=df.loc[:, 'Unnamed: 2': 'Unnamed: 5'], axis=1)
df = df.drop(df.index[6:24], axis=0)
df = df.drop(df.index[15:157], axis=0)
df = df.drop(df.iloc[:, 2:6, ], axis=1)
df = df.drop(df.iloc[:, 3:7, ], axis=1)
df = df.drop(df.iloc[:, 4:8, ], axis=1)
t = pd.DataFrame(df.columns)
t.loc[t[0].str.startswith('Unnamed: '), 0] = ""
t[0].bfill(inplace=True)
df.columns = t[0].values
prcntf = [19.90, 19.90, 27.90, 27.90, 32.90, 32.90, 39.90, 39.90]
Ano0 = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

df1 = pd.read_csv("Datasets/2020.csv", sep=';')
df1 = df1.fillna("")
df1 = df1.drop(columns=df1.loc[:, 'Unnamed: 2': 'Unnamed: 15'], axis=1)
df1 = df1.drop(df1.index[6:24], axis=0)
df1 = df1.drop(df1.index[15:157], axis=0)
df1 = df1.drop(df1.iloc[:, 2:6, ], axis=1)
t = pd.DataFrame(df1.columns)
t.loc[t[0].str.startswith('Unnamed: '), 0] = ""
t[0].bfill(inplace=True)
df1.columns = t[0].values

df2 = pd.read_csv("Datasets/2023-2021.csv", sep=';')
df2 = df2.fillna("")
df2 = df2.drop(columns=df2.loc[:, 'Unnamed: 2': 'Unnamed: 5'], axis=1)
df2 = df2.drop(df2.index[6:24], axis=0)
df2 = df2.drop(df2.index[15:157], axis=0)
df2 = df2.drop(df2.iloc[:, 2:6, ], axis=1)
df2 = df2.drop(df2.iloc[:, 3:7, ], axis=1)
df2 = df2.drop(df2.iloc[:, 4:6, ], axis=1)
t = pd.DataFrame(df2.columns)
t.loc[t[0].str.startswith('Unnamed: '), 0] = ""
t[0].bfill(inplace=True)
df2.columns = t[0].values

a = df.iloc[5, 2:5].to_numpy(copy=True)
a = np.append(a, df1.iloc[5, 2])
b = df2.iloc[5, 2:5].to_numpy(copy=True)
Ano1 = np.concatenate((a, b))

a = df.iloc[10, 2:5].to_numpy(copy=True)
a = np.append(a, df1.iloc[10, 2])
b = df2.iloc[10, 2:5].to_numpy(copy=True)
Assin = np.concatenate((a, b))

for j in range(len(Assin)):
    Assin[j] = Assin[j].replace('.', '')
    Assin[j] = Assin[j].strip()

Asnt = [float(i) for i in Assin]
An1 = [int(i) for i in Ano1]


def assinantes_netflix():
    fig = px.line(x=An1, y=Asnt)
    fig.update_xaxes(title_text="Ano")
    fig.update_yaxes(title_text="Em milhares")
    st.plotly_chart(fig, use_container_width=True)
# ______________________________________________________________________________________________________________


# _____Dataset Bilheteria_______________________________________________________________________________________
df3 = pd.read_csv("Datasets/Bilheteria.csv", sep=';')
t = pd.DataFrame(df3.columns)
t.loc[t[0].str.startswith('Unnamed: '), 0] = ""
t[0].bfill(inplace=True)
df3.columns = t[0].values
Ano2 = df3.iloc[0, 1:22].to_numpy(copy=True)
publico = df3.iloc[1, 1:22].to_numpy(copy=True)
part = df3.iloc[4, 1:22].to_numpy(copy=True)
prec = df3.iloc[13, 1:22].to_numpy(copy=True)
for j in range(len(publico)):
    publico[j] = publico[j].replace('.', '')
    publico[j] = publico[j].strip()
pbl = [int(i) for i in publico]
lanc = df3.iloc[11, 1:22].to_numpy(copy=True)
for j in range(len(lanc)):
    lanc[j] = lanc[j].replace('%', '')
    lanc[j] = lanc[j].replace(',', '.')
    lanc[j] = lanc[j].strip()
    part[j] = part[j].replace('%', '')
    part[j] = part[j].replace(',', '.')
    part[j] = part[j].strip()
    prec[j] = prec[j].replace(',', '.')
    prec[j] = prec[j].strip()
An2 = [int(i) for i in Ano2]
lnc = [float(i) for i in lanc]
prt = [float(i) for i in part]
prc = [float(i) for i in prec]
plbcmp = pbl[15:21]
anocmp = An1[0:6]
asscmp = Asnt[0:6]

frqcim = pd.DataFrame({'ANO': anocmp, 'Publico de cinema': plbcmp, 'Assinantes netflix': asscmp})
frqcim.set_index('ANO', inplace=True)
frqcim = frqcim.pct_change()*100


def bilheteria():
    fig = frqcim.plot(title="Bilheteria", labels=dict(index="Ano", value="Em porcentagem",
                                                      variable=""))
    st.plotly_chart(fig, use_container_width=True)
# ______________________________________________________________________________________________________________


# _____Publico do cinema________________________________________________________________________________________
pblev = pd.DataFrame({'ANO': An2, 'Publico de cinema': pbl})
pblev.set_index('ANO', inplace=True)


def publico_cinema():
    fig = pblev.plot(title="Publico cinema", labels=dict(index="Ano", value="Em milhares",
                                                         variable=""))
    st.plotly_chart(fig, use_container_width=True)
# ______________________________________________________________________________________________________________


# _____________Participação nacional____________________________________________________________________________
nacfilm = pd.DataFrame({'ANO': An2, 'Participação nacional': prt, 'lançamentos brasileiros': lnc})
nacfilm.set_index('ANO', inplace=True)


def participacao_nacional():
    fig = nacfilm.plot(title="Participação nacional", labels=dict(index="Ano", value="Em porcentagem",
                                                                  variable=""))
    st.plotly_chart(fig, use_container_width=True)
# ______________________________________________________________________________________________________________


# _____Plano padrão netflix VS Preço ingresso___________________________________________________________________
prcmp = prc[13:21]
difval = pd.DataFrame({'ANO': Ano0, 'Plano padrao': prcntf, 'Preço medio ingresso': prcmp})
difval.set_index('ANO', inplace=True)


def plnetflix_x_ingresso():
    fig = difval.plot(title="Consumo VS Lançamentos", labels=dict(index="Ano", value="Em reais",
                                                                  variable=""))
    st.plotly_chart(fig, use_container_width=True)
# ______________________________________________________________________________________________________________


# _____Dados Econômicos_________________________________________________________________________________________
df4 = pd.read_csv("Datasets/Dados_Economicos.csv", sep=';')
t = pd.DataFrame(df4.columns)
t.loc[t[0].str.startswith('Unnamed: '), 0] = ""
t[0].bfill(inplace=True)
df4.columns = t[0].values
df4 = df4.fillna("")

sal_min = df4.iloc[4, 1:22].to_numpy(copy=True)

for j in range(len(sal_min)):
    sal_min[j] = sal_min[j].replace('.', '')
    sal_min[j] = sal_min[j].replace(',', '.')
    sal_min[j] = sal_min[j].strip()

Slmin = [float(i) for i in sal_min]

df41 = pd.DataFrame({'ANO': An2, 'Salario minimo': Slmin, 'Preco medio ingresso': prc})
df41.set_index('ANO', inplace=True)

df41 = df41.pct_change()*100


def salario_x_ingresso():
    fig = df41.plot(title="Salário Mínimo VS Valor ingresso", labels=dict(index="Ano", value="Em percentual",
                                                                          variable=""))

    st.plotly_chart(fig, use_container_width=True)
# ______________________________________________________________________________________________________________


# ___________Domicílios com acesso a internet___________________________________________________________________
df5 = pd.read_csv("Datasets/domicilios_acesso.csv", encoding='latin-1', sep=';')
df5 = df5.drop(['Unnamed: 3', 'Unnamed: 5', 'Unnamed: 7', 'Unnamed: 9', 'Unnamed: 11',
                'Unnamed: 13', 'Unnamed: 15', 'Unnamed: 17'], axis=1)
df5 = df5.fillna("")
Ano4 = df5.iloc[1, 2:10].to_numpy(copy=True)
acesso = df5.iloc[2, 2:10].to_numpy(copy=True)
df51 = pd.DataFrame({'Ano': Ano4, 'Acesso a internet/domicílio': acesso/1000})
df51.set_index('Ano', inplace=True)


def domicilios_internet():
    fig = df51.plot(title="Acesso a internet/domicílio", labels=dict(index="Ano", value="Em percentual",
                                                                     variable=""))

    st.plotly_chart(fig, use_container_width=True)
# ______________________________________________________________________________________________________________


# ___Salas em funcionamento x Acesso a internet por domicílio___________________________________________________
df6 = pd.read_excel("Datasets/num_salas.xlsx")
salas = df6.iloc[0, 14:22].to_numpy(copy=True)
sxa = pd.DataFrame({'ANO': Ano4, 'Salas em funcionamento': salas, 'Acesso a internet/domicílio': acesso})
sxa.set_index('ANO', inplace=True)
sxa = sxa.pct_change()*100


def salas_x_internet():
    fig = sxa.plot(title="Salas em funcionamento x Acesso a internet por domicílio",
                   labels=dict(index="Ano", value="Em percentual", variable=""))

    st.plotly_chart(fig, use_container_width=True)
# ______________________________________________________________________________________________________________
