# 📊 Análise de Indicadores Empresariais com Python

Projeto em Python para **análise de indicadores empresariais**, utilizando dados mensais de desempenho para gerar **diagnósticos automáticos**, **alertas** e um **resumo executivo** com apoio da biblioteca **pandas**.

O objetivo é demonstrar, de forma prática, como dados podem apoiar a tomada de decisão em um cenário empresarial.

---

## 🧠 Funcionalidades

- Leitura de dados a partir de arquivo CSV  
- Análise estatística descritiva dos indicadores  
- Identificação automática de:
  - Meses com prejuízo
  - Reclamações acima da média
  - Queda no número de clientes ativos
  - Tempo médio de atendimento acima do esperado
- Classificação dos meses por status:
  - 🟢 Estável
  - 🟡 Atenção
  - 🔴 Crítico
- Geração de um **resumo executivo** com os principais insights

---

## 📁 Estrutura do Projeto

├── analise_indicadores.py # Script principal de análise
├── dados.csv # Base de dados utilizada
├── relatorio_analise.txt # Saída textual da análise
├── README.md # Documentação do projeto
└── .gitignore # Arquivos ignorados pelo Git


---

## 📊 Dados Utilizados

O arquivo `dados.csv` contém os seguintes campos:

- `mes`
- `receita`
- `custos`
- `lucro`
- `clientes_ativos`
- `reclamacoes`
- `tempo_medio_atendimento`

Exemplo de registro:
```csv
Janeiro,120000,80000,40000,1500,180,8

▶️ Como Executar o Projeto

1️⃣ Clonar o repositório

git clone https://github.com/GohuCarvalho/Analise-de-Indicadores-Empresariais-com-Python.git
cd Analise-de-Indicadores-Empresariais-com-Python

2️⃣ Criar ambiente virtual (opcional, recomendado)

python -m venv .venv
source .venv/bin/activate  # Linux / WSL
# ou
.venv\Scripts\activate     # Windows

3️⃣ Instalar dependências

pip install pandas

4️⃣ Executar o script

python analise_indicadores.py

🧾 Exemplo de Saída

Estatísticas gerais dos indicadores

Lista de meses com prejuízo

Alertas automáticos

Classificação mensal por status

Resumo executivo final com métricas consolidadas


🎯 Objetivo do Projeto

Este projeto foi desenvolvido com fins educacionais e de portfólio, demonstrando:

Manipulação de dados com pandas

Lógica de análise de negócios

Geração de insights automatizados

Organização de um projeto Python versionado com Git e GitHub

🛠 Tecnologias Utilizadas

Python 3

pandas

Git & GitHub

👤 Autor

Hugo Avelino de Carvalho
Projeto desenvolvido como parte do aprendizado em Python e análise de dados.

