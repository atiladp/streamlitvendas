# 📊 Dashboard de Vendas com Streamlit

Este é um projeto de **dashboard interativo** para análise de vendas, construído com **Python e Streamlit**. Ele permite explorar dados de vendas por categoria, estado, vendedor e período de tempo, com gráficos interativos criados com Plotly e filtros dinâmicos.

Atualmente, os dados são carregados a partir de um arquivo `.json` e manipulados com Pandas. A integração com banco de dados SQLite está planejada como próxima etapa.

# TESTE DE MARK
---

## 🚀 Funcionalidades

- Visualização completa do dataset de vendas
- Filtros interativos:
  - Categoria do produto
  - Faixa de preço
  - Período da compra
  - Vendedores
- Download dos dados filtrados em `.csv`
- Gráficos:
  - Receita por estado (mapa)
  - Receita mensal
  - Receita por categoria
  - Receita e volume de vendas por vendedor
- Interface intuitiva com navegação por abas

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- JSON como fonte de dados

---

## 🗂️ Estrutura do Projeto

📁 dashboard-vendas/
├── app.py ← Dashboard principal
├── vendas.py ← Página para visualizar/exportar dados
├── graficos.py ← Geração dos gráficos Plotly
├── utils.py ← Funções auxiliares e pré-processamento
├── dataset.py ← Carrega o DataFrame a partir do JSON
├── dados/
│ └── vendas.json ← Arquivo de dados original
├── README.md ← Este arquivo


---

## 📥 Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/dashboard-vendas.git
cd dashboard-vendas

2. (Opcional) Crie um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Instale as dependências:

pip install -r requirements.txt

▶️ Como Rodar

Execute o app com o Streamlit:

streamlit run app.py

📌 Melhorias Futuras

    💾 Integração com banco de dados SQLite3 para persistência

    🧾 Formulário para cadastrar novas vendas diretamente pela interface

    ☁️ Suporte para múltiplos arquivos de entrada (CSV, JSON, Excel)

    👤 Controle de acesso e autenticação de usuários

Autor
Átila Barbosa Daniel
📄 Licença
Este projeto está licenciado sob a MIT License.

