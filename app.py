from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar os clientes
clientes = []

# Lista para armazenar os produtos
produtos = []

# Lista para armazenar os pedidos
pedidos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro_cliente', methods=['GET', 'POST'])
def cadastro_cliente():
    if request.method == 'POST':
        id_cliente = request.form['id']
        nome_cliente = request.form['nome']
        
        # Verificar se o ID ou nome do cliente já existem
        for cliente in clientes:
            if cliente['id'] == id_cliente:
                return 'Erro: Cliente com este ID já existe!'
            if cliente['nome'] == nome_cliente:
                return 'Erro: Cliente com este nome já existe!'
        
        # Se o ID e o nome do cliente forem únicos, adicione o cliente à lista
        clientes.append({'id': id_cliente, 'nome': nome_cliente})
        return redirect(url_for('index'))
    else:
        # Se a solicitação for GET, apenas renderize o formulário de cadastro de cliente
        return render_template('cadastro_cliente.html')
    
@app.route('/cadastro_produto', methods=['GET', 'POST'])
def cadastro_produto():
    if request.method == 'POST':
        id_produto = request.form['id_produto']
        nome_produto = request.form['nome_produto']
        preco_produto = float(request.form['preco_produto'])  # Convertendo o preço para float
        # Verifica se o ID do produto já existe
        for produto in produtos:
            if produto['id'] == id_produto:
                return 'Erro: Produto com este ID já existe!'
        
        # Se o ID do produto for único, adiciona o produto à lista
        produtos.append({'id': id_produto, 'nome': nome_produto, 'preco': preco_produto})
        return redirect(url_for('index'))
    else:
        return render_template('cadastro_produto.html')

    
@app.route('/cadastro_pedido', methods=['GET', 'POST'])
def cadastro_pedido():
    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        cliente = next((c for c in clientes if c['id'] == id_cliente), None)
        if cliente is None:
            return 'Cliente não encontrado!'
        
        # Processa apenas os produtos selecionados e calcula os valores
        produtos_selecionados = []
        total_pedido = 0  # Inicializa o total do pedido
        for produto_id in request.form.getlist('produtos'):
            produto = next((p for p in produtos if p['id'] == produto_id), None)
            if produto is not None:
                quantidade = int(request.form.get(f'quantidade_{produto_id}', 1))  # Obtém a quantidade ou usa 1 como padrão
                valor_total_item = produto['preco'] * quantidade  # Calcula o valor total do item
                total_pedido += valor_total_item  # Adiciona ao total do pedido
                produtos_selecionados.append({'produto': produto, 'quantidade': quantidade, 'valor_total_item': valor_total_item})

        # Verifica se o pedido está vazio
        if not produtos_selecionados:
            return 'Erro: O pedido não pode estar vazio!'

        # Cria o pedido e adiciona à lista de pedidos
        pedido = {'cliente': cliente, 'produtos': produtos_selecionados, 'total_pedido': total_pedido}
        pedidos.append(pedido)
        
        # Redireciona para a página inicial
        return redirect(url_for('index'))
    else:
        return render_template('cadastro_pedido.html', clientes=clientes, produtos=produtos)


@app.route('/todas_as_vendas')
def todas_as_vendas():
    return render_template('todas_as_vendas.html', pedidos=pedidos)

if __name__ == '__main__':
    app.run(debug=True)
