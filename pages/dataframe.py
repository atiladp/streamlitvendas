# Importa a biblioteca Streamlit para criar a interface web
import streamlit as st

# Importa o DataFrame com os dados de vendas
from dataset import df

# Importa as funções utilitárias para conversão de CSV e exibição de mensagens
from utils import convert_csv, mensagem_sucesso

# Define o título da página
st.title('Dataset de Vendas')

# Cria uma seção expansível para seleção de colunas do DataFrame
with st.expander('Colunas'):
    # Cria um seletor múltiplo para que o usuário escolha quais colunas deseja visualizar
    colunas = st.multiselect(
        'Selecione as Colunas',
        list(df.columns),  # Todas as colunas disponíveis
        list(df.columns)   # Seleciona todas por padrão
    )

# Cria um título na barra lateral para os filtros
st.sidebar.title('Filtros')

# Filtro por Categoria do Produto (em expander na sidebar)
with st.sidebar.expander('Categoria do Produto'):
    categorias = st.multiselect(
        'Selecione as categorias',
        df['Categoria do Produto'].unique(),  # Lista única de categorias
        df['Categoria do Produto'].unique()   # Seleciona todas por padrão
    )

# Filtro por faixa de preço (em expander na sidebar)
with st.sidebar.expander('Preço do Produto'):
    preco = st.slider(
        'Selecione o Preço',
        0, 5000,            # Faixa de valores possíveis
        (0, 5000)           # Valor inicial do seletor (seleciona toda a faixa)
    )

# Filtro por intervalo de datas (em expander na sidebar)
with st.sidebar.expander('Data da Compra'):
    data_compra = st.date_input(
        'Selecione a data',
        (df['Data da Compra'].min(),  # Data mínima do dataset
         df['Data da Compra'].max())  # Data máxima do dataset
    )

# Cria uma string de consulta com base nos filtros selecionados
query = '''
    `Categoria do Produto` in @categorias and \
    @preco[0] <= Preço  <= @preco[1] and \
    @data_compra[0] <= `Data da Compra` <= @data_compra[1]
'''

# Filtra o DataFrame usando a query construída
filtro_dados = df.query(query)

# Seleciona apenas as colunas escolhidas pelo usuário
filtro_dados = filtro_dados[colunas]

# Exibe o DataFrame filtrado na tela
st.dataframe(filtro_dados)

# Mostra o número de linhas e colunas da tabela filtrada
st.markdown(f'A tabela possui :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] colunas')

# Texto para instruir o usuário a nomear o arquivo que será baixado
st.markdown('Escreva um nome do arquivo')

# Divide a área da interface em duas colunas para o input e o botão de download
coluna1, coluna2 = st.columns(2)

with coluna1:
    # Campo de entrada de texto para o nome do arquivo
    nome_arquivo = st.text_input(
        '',
        label_visibility='collapsed'  # Oculta o rótulo do input
    )
    # Adiciona extensão .csv ao nome do arquivo
    nome_arquivo += '.csv'

with coluna2:
    # Cria um botão para download do arquivo CSV
    st.download_button(
        'Baixar arquivo',
        data=convert_csv(filtro_dados),  # Converte os dados filtrados em CSV
        file_name=nome_arquivo,          # Usa o nome informado pelo usuário
        mime='text/csv',                 # Define o tipo MIME como CSV
        on_click=mensagem_sucesso        # Exibe mensagem de sucesso ao clicar
    )
