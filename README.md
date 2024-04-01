# Documentação da Aplicação de Gerenciamento de Pedidos
## Introdução
Esta documentação descreve a estrutura e o funcionamento da aplicação de gerenciamento de pedidos desenvolvida utilizando Flask.

## Funcionalidades
A aplicação possui as seguintes funcionalidades:

- Cadastro de Clientes 
- Cadastro de Produtos 
- Cadastro de Pedidos  
- Visualização de todas as vendas 
## Estrutura do Projeto
A estrutura do projeto é a seguinte:

- ├── app.py
- ├── templates
- │   ├── cadastro_cliente.html
- │   ├── cadastro_pedido.html
- │   ├── cadastro_produto.html
- │   └── todas_as_vendas.html
- └── static
-    └── style.css

app.py: Arquivo principal que contém a lógica da aplicação Flask.\
templates: Pasta que contém os arquivos HTML para as diferentes páginas da aplicação.\
static: Pasta que contém arquivos estáticos, como folhas de estilo CSS.
## Como Executar
Para executar a aplicação, siga estas etapas:

1. Certifique-se de ter o Python e o Flask instalados em seu ambiente.

2. Clone o repositório do projeto.

3. Navegue até o diretório do projeto no terminal.

4. Execute o seguinte comando para iniciar a aplicação: python app.py

5. Abra um navegador da web e acesse http://localhost:5000 para acessar a aplicação.

## Como Utilizar
- Cadastro de Clientes: Na página inicial, clique em "Cadastro de Clientes" e preencha o formulário com o ID e nome do cliente.
- Cadastro de Produtos: Da mesma forma, clique em "Cadastro de Produtos" e preencha o formulário com o ID, nome e preço do produto.
- Cadastro de Pedidos: Na página inicial, clique em "Cadastro de Pedidos" e selecione um cliente e os produtos desejados, informando também a quantidade de cada produto.
- Visualização de Todas as Vendas: Clique em "Todas as Vendas" na página inicial para visualizar todos os pedidos cadastrados.
## Autor
Este projeto foi desenvolvido por Rodrigo Cavalcanti Cabral.

