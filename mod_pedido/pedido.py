#coding: utf-8
from flask import Blueprint, render_template, request, jsonify, json

from mod_login.login import validaSessao
from mod_pedido.pedidoBD import Pedidos, PedidosProdutos
from mod_produto.produtoBD import Produtos
from mod_cliente.clienteBD import Clientes

bp_pedido = Blueprint('pedidos',__name__, url_prefix='/pedidos', template_folder='templates')

@bp_pedido.route("/")
@validaSessao
def formListaPedidos():
    _pedido = Pedidos()
    _lista_pedidos = _pedido.selectAll()

    _produto = Produtos()
    _lista_produtos = _produto.selectAll()
    return render_template("formListaPedidos.html", pedidos = _lista_pedidos, produtos = _lista_produtos)

@bp_pedido.route("/formPedido")
@validaSessao
def formPedido():
    _produto = Produtos()
    _lista_produtos = _produto.selectAll()    
    _pedido = Pedidos()
    return render_template("formPedido.html", produtos = _lista_produtos, pedido = _pedido)

@bp_pedido.route("/formEditPedido", methods = ['POST'])
@validaSessao
def formEditPedido():
    _pedido = Pedidos()
    _pedido.id_pedido = request.form['id_pedido']
    _pedido.selectOne()

    _produto = Produtos()
    _lista_produtos = _produto.selectAll()    

    return render_template('formPedido.html', pedido = _pedido, produtos = _lista_produtos)
@bp_pedido.route("/buscaClienteById", methods = ['POST'])
@validaSessao
def buscaClienteById():
    try:
        _cliente = Clientes()
        _cliente.id_cliente = request.form['id_cliente']
        _cliente.selectOne()
        _cliente_encontrado = _cliente.nome != ""
        clienteJson = _cliente.toJSON()

        return jsonify(erro = False, cliente_encontrado = _cliente_encontrado, cliente = clienteJson)

    
    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
            return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)
        else:
            return jsonify(erro = True,mensagem = "Erro ao tentar buscar cliente!" ,mensagem_exception = str(e))

@bp_pedido.route("/buscaProdutoById", methods = ['POST'])
@validaSessao
def buscaProdutoById():
    try:
        _produto = Produtos()
        _produto.id_produto = request.form['id_produto']
        _produto.selectONE()
        _produtoJson = _produto.toJSON()

        return jsonify(erro = False, produto = _produtoJson)

    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
            return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)
        else:
            return jsonify(erro = True,mensagem = "Erro ao tentar buscar produto!" ,mensagem_exception = str(e))

@bp_pedido.route("/addPedido", methods = ['POST'])
@validaSessao
def addPedido():
    try:
        _pedido = Pedidos()        
        _pedido.id_cliente = request.form['id_cliente']
        _pedido.data_hora = request.form['data_hora']
        _pedido.observacao = request.form['observacao']

        _mensagem = _pedido.insert()

        return jsonify(erro = False, mensagem = _mensagem )
    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
            return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)
        else:
            return jsonify(erro = True,mensagem = "Erro ao tentar adicionar pedido!" ,mensagem_exception = str(e))

@bp_pedido.route("/addProdutoPedido", methods = ['POST'])
@validaSessao
def addProdutoPedido():
    try:
        _pedido_produto = PedidosProdutos()
        _pedido_produto.id_pedido = request.form['id_pedido']
        _pedido_produto.id_produto = request.form['id_produto']
        _pedido_produto.quantidade = request.form['quantidade']
        _pedido_produto.valor = request.form['valor']
        _pedido_produto.observacao = request.form['observacao']

        _mensagem = _pedido_produto.insertProdutosPedido()

        return jsonify(erro = False, mensagem = _mensagem)

    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
            return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)
        else:
            return jsonify(erro = True,mensagem = "Erro ao tentar adicionar produtos no pedido!" ,mensagem_exception = str(e))

@bp_pedido.route("/selectProdutosByPedido", methods = ['POST'])
@validaSessao
def selectProdutosByPedido():
    try:
        _pedido_produto = PedidosProdutos()
        _pedido_produto.id_pedido = request.form['id_pedido']
        _lista_produtos =  _pedido_produto.selectProdutosByPedido()

        return jsonify(erro = False, produtos = _lista_produtos)
    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
            return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)
        else:
            return jsonify(erro = True,mensagem = "Erro ao tentar buscar produtos do pedido!" ,mensagem_exception = str(e))
