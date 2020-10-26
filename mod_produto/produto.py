#coding: utf-8
from flask import Blueprint, render_template, request, jsonify
import base64

from mod_login.login import validaSessao
from mod_produto.produtoBD import Produtos

bp_produto = Blueprint('produto', __name__, url_prefix='/produto', template_folder='templates')

@bp_produto.route("/")
@validaSessao
def formListaProdutos():
    return render_template("formListaProdutos.html")

@bp_produto.route("/formProduto")
@validaSessao
def formProduto():
    return render_template("formProduto.html")

@bp_produto.route("/addProduto", methods = ['POST'])
@validaSessao
def addProduto():
    try:
        
        _produto = Produtos()
        _produto.descricao = request.form['descricao']
        _produto.valor = request.form['valor']
        _produto.imagem = base64.b64encode(bytearray(request.form['imagem'],'utf-8'))

        _mensagem = _produto.insert()

        return jsonify(erro = False, mensagem = _mensagem)

    except Exception as e:
        if len(e.args)> 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)


