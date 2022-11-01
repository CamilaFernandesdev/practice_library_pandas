# %% [markdown]
# # Análise de Dados
#
# Relatórios de vendas em diferentes cidades
#
# Índice
# 1. [Extraindo os dados](#extraindo-os-dados)
# 1. [Análise do Faturamento](#faturamento)
# 2. [Análise das lojas](#análise-das-lojas)
# 1. [Visualização dos dados][def]
#
#
#
# [def]: #visualização-dos-dados

# %% [markdown]
# ### Extraindo os dados

# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%

# Relatórios de vendas em cada cidade
df_aracaju = pd.read_excel('datasets/Aracaju.xlsx')
df_fortaleza = pd.read_excel('datasets/Fortaleza.xlsx')
df_natal = pd.read_excel('datasets/Natal.xlsx')
df_recife = pd.read_excel('datasets/Recife.xlsx')
df_salvador = pd.read_excel('datasets/Salvador.xlsx')

# %%
df_vendas = pd.concat([df_aracaju,
                       df_fortaleza,
                       df_natal,
                       df_recife,
                       df_salvador])

df_vendas

# %%
# verificando os dados
df_vendas.sample(7)

# %%
# Modificando os parâmetros das colunas

# "LojaID" por se tratar de um código que não será calculado
df_vendas['LojaID'] = df_vendas['LojaID'].astype('object')

# Convertendo coluna 'Datas' em datetime
df_vendas['Data'] = df_vendas['Data'].astype('int64')
df_vendas['Data'] = pd.to_datetime(df_vendas['Data'])
df_vendas.dtypes

# %%
# Verificando valores nulos
df_vendas.isnull().sum()

# %% [markdown]
# ### Faturamento

# %%
# Total de vendas
df_vendas['Receita'] = df_vendas['Vendas'].mul(df_vendas['Qtde'])
df_vendas.sample(5)

# %% [markdown]
# Quais foram as 5 maiores vendas?

# %%
# Retorna as maiores e as menores receitas
df_vendas.nlargest(n=5, columns='Receita')

# %% [markdown]
# E as 5 menores receitas?

# %%
df_vendas.nsmallest(n=5, columns='Receita')

# %% [markdown]
# Qual a quantidade de venda por cidade?

# %%
df_vendas.groupby('Cidade')['Receita'].sum()

# %% [markdown]
# Houve aumento das vendas no decorrer dos anos?

# %%
df_vendas.groupby(df_vendas['Data'].dt.year)['Receita'].sum()

# %% [markdown]
# Como foi o desempenho por ano?

# %%
df_vendas2019 = df_vendas.loc[(df_vendas['Data'].dt.year == 2019)]
df_vendas2019.groupby(df_vendas2019['Data'].dt.month)['Receita'].sum()

# %%
df_vendas2018 = df_vendas.loc[(df_vendas['Data'].dt.year == 2018)]
df_vendas2018.groupby(df_vendas2018['Data'].dt.month)['Receita'].sum()

# %% [markdown]
# Como foi o faturamento no decorrer dos meses?

# %%
df_vendas.groupby(df_vendas['Data'].dt.month)['Receita'].sum()

# %% [markdown]
# E o faturamento trimestral?

# %%
df_vendas['Trimestre'] = df_vendas['Data'].dt.quarter
df_vendas.groupby('Trimestre')['Receita'].sum()

# %% [markdown]
# Média por mes

# %%
df_vendas.groupby(df_vendas['Data'].dt.month)['Receita'].mean()

# %% [markdown]
# ### Análise das lojas

# %% [markdown]
# Quantidade de vendas por loja

# %%
df_vendas['LojaID'].value_counts(ascending=False)

# %% [markdown]
# ### Visualização dos Dados

# %% [markdown]
# Quantidade de vendas por loja

# %%
df_vendas['LojaID'].value_counts(ascending=False).plot.bar()

# %% [markdown]
# Receita por ano

# %%
df_vendas.groupby(df_vendas['Data'].dt.year)['Receita'].sum().plot.pie()

# %% [markdown]
# Vendas por cidade

# %%

df_vendas['Cidade'].value_counts().plot.bar(title='Total de vendas por cidade',
                                            color='red')
plt.xlabel('Cidade')
plt.ylabel('Total de Vendas')

# %% [markdown]
# Personalizando a apresentação dos gráficos

# %%
plt.style.use('ggplot')

# %% [markdown]
# Receita por mês

# %%
df_vendas.groupby(df_vendas['Data'].dt.month)['Receita'].sum().plot.bar()
plt.xlabel('Mês')
plt.ylabel('Total de Produtos Vendidos')
plt.legend()

# %%
df_vendas2019.groupby(df_vendas2019['Data'].dt.day)[
    'Qtde'].sum().plot(marker='o')
plt.xlabel('Dias')
plt.ylabel('Total de produtos vendidos')
plt.legend()

# %% [markdown]
# Quantidade de vendas por cidade em 2018

# %%
plt.scatter(x=df_vendas2018['Data'].dt.month,
            y=df_vendas2018['Receita'])
