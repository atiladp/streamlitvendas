# Importa o módulo json para trabalhar com arquivos JSON
import json

# Importa o pandas para manipulação de dados em formato tabular (DataFrame)
import pandas as pd

# Abre o arquivo JSON com os dados de vendas (modo leitura padrão)
file = open('dados/vendas.json')

# Carrega o conteúdo do arquivo JSON em um dicionário Python
data = json.load(file)

# Converte o dicionário em um DataFrame do pandas
df = pd.DataFrame.from_dict(data)

# Converte a coluna "Data da Compra" de string para formato datetime
# Define o formato esperado como 'dia/mês/ano'
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

# Fecha o arquivo JSON após o uso
file.close()
