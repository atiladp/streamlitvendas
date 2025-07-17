# Importa a biblioteca Streamlit para criar aplicações web interativas
import streamlit as st

# Importa a biblioteca Plotly Express para criação de gráficos interativos
import plotly.express as px

# Importa o DataFrame `df` do módulo `dataset`
from dataset import df

# Importa a função `format_number` do módulo `utils` para formatar valores numéricos
from utils import format_number

# Importa as funções que retornam gráficos do módulo `graficos`
from graficos import (
    grafico_map_estado,
    grafico_rec_mensal,
    grafico_rec_estado,
    grafico_rec_categoria,
    grafico_rec_vendedores,
    grafico_vendas_vendedores
)

# Define a configuração da página como layout "wide" (tela cheia)
st.set_page_config(layout='wide')

# Exibe o título principal da aplicação
st.title("Dashboard de Vendas")

# Cria um título na barra lateral
st.sidebar.title('Filtro de Vendedores')

# Cria um filtro múltiplo na barra lateral com os nomes dos vendedores únicos do DataFrame
filtro_vendedor = st.sidebar.multiselect(
    'Vendedores',
    df['Vendedor'].unique(),
)

# Se houver algum vendedor selecionado no filtro, filtra o DataFrame para exibir apenas os dados correspondentes
if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]

# Cria três abas para navegação: Dataset, Receita e Vendedores
aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])

# Conteúdo da aba "Dataset"
with aba1:
    # Exibe o DataFrame completo (ou filtrado) na tela
    st.dataframe(df)

# Conteúdo da aba "Receita"
with aba2:
    # Divide a tela em duas colunas
    coluna1, coluna2 = st.columns(2)

    with coluna1:
        # Exibe o valor total da receita formatado como moeda
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$'))

        # Exibe o gráfico de mapa com receita por estado
        st.plotly_chart(grafico_map_estado, use_container_width=True)

        # Exibe o gráfico de barras com receita por estado
        st.plotly_chart(grafico_rec_estado, use_container_width=True)

    with coluna2:
        # Exibe a quantidade total de vendas (número de linhas do DataFrame)
        st.metric('Quantidade de Vendas', format_number(df.shape[0]))

        # Exibe o gráfico de linha com receita mensal
        st.plotly_chart(grafico_rec_mensal, use_container_width=True)

        # Exibe o gráfico de barras com receita por categoria de produto
        st.plotly_chart(grafico_rec_categoria, use_container_width=True)

# Conteúdo da aba "Vendedores"
with aba3:
    # Divide a aba em duas colunas
    coluna1, coluna2 = st.columns(2)

    with coluna1:
        # Exibe o gráfico de receita por vendedor
        st.plotly_chart(grafico_rec_vendedores)

    with coluna2:
        # Exibe o gráfico de quantidade de vendas por vendedor
        st.plotly_chart(grafico_vendas_vendedores)
