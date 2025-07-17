# Importa o DataFrame df do módulo dataset
from dataset import df

# Importa a biblioteca pandas para manipulação de dados
import pandas as pd

# Importa a biblioteca streamlit para funcionalidades web
import streamlit as st

# Importa a biblioteca time para utilizar a função sleep (pausa)
import time

# Função para formatar números com prefixos e unidades simplificadas
def format_number(value, prefix = ''):
    # Loop para verificar se o valor deve ser representado em mil ou milhões
    for unit in ['', 'mil']:
        if value < 1000:
            # Retorna o valor formatado com duas casas decimais e unidade apropriada
            return f'{prefix} {value:.2f} {unit}'
        # Divide o valor por 1000 para converter para mil ou milhões
        value /= 1000
    # Retorna valor em milhões
    return f'{prefix} {value:.2f} milhões'

# -------------------- CRIAÇÃO DE DATAFRAMES DERIVADOS --------------------

# 1 - DataFrame de Receita por Estado
# Agrupa o DataFrame original por local da compra, somando os valores da coluna 'Preço'
df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()

# Remove duplicatas para cada local da compra, mantendo lat/lon, e junta com as somas calculadas
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']] \
    .merge(df_rec_estado, left_on='Local da compra', right_index=True) \
    .sort_values('Preço', ascending=False)

# 2 - DataFrame de Receita Mensal
# Define o índice do DataFrame como a data da compra e agrupa por mês, somando a receita
df_rec_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))['Preço'].sum().reset_index()

# Extrai o ano da data da compra para nova coluna
df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year

# Extrai o nome do mês da data da compra para nova coluna
df_rec_mensal['Mes'] = df_rec_mensal['Data da Compra'].dt.month_name()

# 3 - DataFrame de Receita por Categoria de Produto
# Agrupa os dados por categoria e soma os preços, ordenando do maior para o menor
df_rec_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)

# 4 - DataFrame de Vendedores
# Agrupa por vendedor e calcula duas métricas: soma da receita e contagem de vendas
df_vendedores = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum', 'count']))

# -------------------- FUNÇÕES DE UTILIDADE PARA A INTERFACE --------------------

# Função que converte um DataFrame para CSV codificado em UTF-8 (para download)
@st.cache_data  # Usa cache para acelerar em chamadas repetidas
def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')

# Função para exibir uma mensagem de sucesso temporária
def mensagem_sucesso():
    # Mostra uma mensagem de sucesso com ícone
    success = st.success(
        'Arquivo baixado com sucesso',
        icon="✅"
    )
    # Aguarda 3 segundos
    time.sleep(3)
    # Remove a mensagem da tela
    success.empty()
