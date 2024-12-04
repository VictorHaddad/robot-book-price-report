
# Scraper de Livros e Geração de Relatório

Este projeto automatiza a coleta de dados sobre livros de um site de exemplos, realiza a análise dos dados coletados (como preço médio e livros caros), e gera relatórios em PDF sobre esses livros. Ele utiliza o `BeautifulSoup` para scraping de dados, `Pandas` para manipulação de dados e `ReportLab` para a geração de relatórios em PDF. Além disso, armazena informações no banco de dados MongoDB.

## Funcionalidades

1. **Coleta de Dados de Livros**:
    - Realiza scraping em páginas de livros de um site de exemplo (Books to Scrape).
    - Coleta informações como título, preço e disponibilidade de cada livro.
    - Armazena os dados coletados em um arquivo CSV.

2. **Análise de Dados**:
    - Filtra livros com preço superior a $20.
    - Calcula o preço médio dos livros.
    - Conta o número total de livros e quantos estão disponíveis.

3. **Geração de Relatório PDF**:
    - Gera um relatório em PDF com informações detalhadas sobre livros caros e resumos do preço médio, total de livros e disponibilidade.
    - Usa a biblioteca `ReportLab` para gerar e formatar o PDF.

4. **Integração com MongoDB**:
    - Registra eventos e erros no banco de dados MongoDB durante o processo de scraping e geração de relatórios.

## Tecnologias Utilizadas

* [Python](https://www.python.org/) 3.12.6
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - Para scraping de dados web
* [Pandas](https://pandas.pydata.org/) - Para manipulação de dados
* [ReportLab](https://www.reportlab.com/) - Para geração de relatórios em PDF
* [MongoDB](https://www.mongodb.com/) - Banco de dados para registro de eventos e erros

## Pré-requisitos

Certifique-se de ter alguma versão do Python instalada e as bibliotecas necessárias no seu ambiente de desenvolvimento.

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu_usuario/scraper-livros-relatorio
    ```

2. Crie um ambiente virtual:
    ```sh
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    * No Windows:
        ```sh
        venv\Scripts\activate
        ```

    * No macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Configuração

1. **Configuração do MongoDB**: O projeto utiliza o MongoDB para registrar eventos e erros. Certifique-se de ter o MongoDB configurado e acessível.
   
2. **Caminho de Salvamento de Arquivos**: Modifique os caminhos de salvamento para os arquivos CSV e PDF de acordo com a sua máquina, caso necessário:
    ```python
    output_file = r"C:\Users\seu_usuario\Desktop\robot\docs\books_data.csv"
    output_pdf = r'C:\Users\seu_usuario\Desktop\robot\docs\books_report.pdf'
    ```

## Uso/Exemplo

Para iniciar a coleta de dados, manipulação e geração de relatório em PDF, execute o seguinte comando:

```sh
python main.py
```

O script irá:
1. Realizar o scraping dos livros do site.
2. Salvar os dados em um arquivo CSV.
3. Gerar um relatório PDF com informações sobre os livros caros e um resumo geral.

## Estrutura de Diretórios

```
scraper-livros-relatorio/
├── main.py                # Arquivo principal com a lógica do scraper e geração de relatórios
├── requirements.txt       # Lista de dependências do projeto
├── docs/                  # Diretório de saída dos arquivos CSV e PDF
├── database/              # Módulo para interação com o MongoDB
└── README.md              # Este arquivo
```