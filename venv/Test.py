import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from pandas.core.groupby import NamedAgg

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
prcntf = [19.90, 19.90, 27.90, 27.90, 32.90, 32.90, 39.90, 39.90]
Ano0 = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

a = df.iloc[5, 2:5].to_numpy(copy=True)
a = np.append(a, df1.iloc[5, 2])
b = df2.iloc[5, 2:5].to_numpy(copy=True)
Ano1 = np.concatenate((a, b))
print(Ano1)

print("\n"*2)

c = df.iloc[10, 2:5].to_numpy(copy=True)
c = np.append(c, df1.iloc[10, 2])
d = df2.iloc[10, 2:5].to_numpy(copy=True)
Assin = np.concatenate((c, d))

for j in range(len(Assin)):
    Assin[j] = Assin[j].replace('.', '')
    Assin[j] = Assin[j].strip()

Asnt = [float(l) for l in Assin]
An1 = [int(l) for l in Ano1]

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
pbl = [int(l) for l in publico]
lanc=df3.iloc[11, 1:22].to_numpy(copy=True)
for j in range(len(lanc)):
    lanc[j] = lanc[j].replace('%', '')
    lanc[j] = lanc[j].replace(',', '.')
    lanc[j] = lanc[j].strip()
    part[j] = part[j].replace('%', '')
    part[j] = part[j].replace(',', '.')
    part[j] = part[j].strip()
    prec[j] = prec[j].replace(',', '.')
    prec[j] = prec[j].strip()
An2= [int(l) for l in Ano2]
lnc = [float(l) for l in lanc]
prt = [float(l) for l in part]
prc = [float(l) for l in prec]
plbcmp = pbl[15:21]
anocmp = An1[0:6]
asscmp = Asnt[0:6]

frqcim = pd.DataFrame({'ANO': anocmp, 'Publico de cinema': plbcmp, 'Assinantes netflix': asscmp})
frqcim.set_index('ANO', inplace=True)
frqcim = frqcim.pct_change()*100
ax = sns.lineplot(data=frqcim)
ax.set_xticks([2018, 2019, 2020, 2021, 2022])
ax.set_ylabel("Em percentual")

