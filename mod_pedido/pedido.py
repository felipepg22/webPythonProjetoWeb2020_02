#coding: utf-8
from flask import Blueprint, render_template, request, jsonify, json

from mod_login.login import validaSessao
from mod_pedido.pedidoBD import Pedidos
from mod_produto.produtoBD import Produtos
from mod_cliente.clienteBD import Clientes

bp_pedido = Blueprint('pedidos',__name__, url_prefix='/pedidos', template_folder='templates')

@bp_pedido.route("/")
@validaSessao
def formListaPedidos():
    _pedido = Pedidos()
    _lista_pedidos = _pedido.selectAll()
    return render_template("formListaPedidos.html", pedidos = _lista_pedidos)

@bp_pedido.route("/formPedido")
@validaSessao
def formPedido():
    _produto = Produtos()
    _lista_produtos = _produto.selectAll()
    _pedido = Pedidos()
    return render_template("formPedido.html", produtos = _lista_produtos, pedido = _pedido)

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