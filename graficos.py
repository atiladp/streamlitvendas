# Importa a biblioteca Plotly Express para criar gráficos interativos
import plotly.express as px

# Importa os DataFrames processados do módulo utils
from utils import df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores

# -------------------- Gráfico 1: Receita por Estado (Mapa) --------------------
grafico_map_estado = px.scatter_geo(
    df_rec_estado,              # DataFrame com localizações e receita por estado
    lat='lat',                  # Coluna com latitude
    lon='lon',                  # Coluna com longitude
    scope='south america',      # Define o escopo geográfico do mapa
    size='Preço',               # Tamanho do ponto proporcional à receita
    template='seaborn',         # Estilo visual do gráfico
    hover_name='Local da compra',  # Nome mostrado ao passar o mouse
    hover_data={'lat': False, 'lon': False},  # Oculta lat/lon no hover
    title='Receita por Estado'  # Título do gráfico
)

# -------------------- Gráfico 2: Receita Mensal (Linha) --------------------
grafico_rec_mensal = px.line(
    df_rec_mensal,              # DataFrame com receita por mês
    x='Mes',                    # Eixo X: nome do mês
    y='Preço',                  # Eixo Y: valor da receita
    markers=True,               # Adiciona marcadores nos pontos
    range_y=(0, df_rec_mensal.max()),  # Define o intervalo do eixo Y
    color='Ano',                # Diferencia linhas por ano
    line_dash='Ano',            # Diferencia o estilo da linha por ano
    title='Receita Mensal'      # Título do gráfico
)

# Atualiza o rótulo do eixo Y
grafico_rec_mensal.update_layout(yaxis_title='Receita')

# -------------------- Gráfico 3: Top 7 Estados por Receita (Barras) --------------------
grafico_rec_estado = px.bar(
    df_rec_estado.head(7),      # Usa os 7 estados com maior receita
    x='Local da compra',        # Eixo X: nome do estado
    y='Preço',                  # Eixo Y: valor da receita
    text_auto=True,             # Mostra o valor em cima das barras
    title='Top Receita por Estados'  # Título do gráfico
)

# -------------------- Gráfico 4: Top 7 Categorias com Maior Receita (Barras) --------------------
grafico_rec_categoria = px.bar(
    df_rec_categoria.head(7),   # Usa as 7 categorias com maior receita
    text_auto=True,             # Mostra os valores nas barras
    title='Top 7 Categorias com Maior Receita'  # Título do gráfico
)

# -------------------- Gráfico 5: Top 7 Vendedores por Receita (Barras Horizontais) --------------------
grafico_rec_vendedores = px.bar(
    df_vendedores[['sum']].sort_values('sum', ascending=False).head(7),  # Top 7 por receita
    x='sum',                                                      # Eixo X: valor da receita
    y=df_vendedores[['sum']].sort_values('sum', ascending=False).head(7).index,  # Eixo Y: nome do vendedor
    text_auto=True,                                               # Mostra valores nas barras
    title='Top 7 Vendedores por Receita'                          # Título do gráfico
)

# -------------------- Gráfico 6: Top 7 Vendedores por Quantidade de Vendas --------------------
grafico_vendas_vendedores = px.bar(
    df_vendedores[['count']].sort_values('count', ascending=False).head(7),  # Top 7 por número de vendas
    x='count',                                                      # Eixo X: quantidade de vendas
    y=df_vendedores[['count']].sort_values('count', ascending=False).head(7).index,  # Eixo Y: nome do vendedor
    text_auto=True,                                                 # Mostra valores nas barras
    title='Top 7 Vendedores por Venda'                              # Título do gráfico
)
