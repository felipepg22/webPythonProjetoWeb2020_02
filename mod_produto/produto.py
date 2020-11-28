#coding: utf-8
from flask import Blueprint, render_template, request, jsonify, send_file
import base64

from mod_login.login import validaSessao
from mod_produto.produtoBD import Produtos
from classeGeraPdf import PDF

bp_produto = Blueprint('produto', __name__, url_prefix='/produto', template_folder='templates')

@bp_produto.route("/")
@validaSessao
def formListaProdutos():
    _produto = Produtos()
    _lista = _produto.selectAll()   

    return render_template("formListaProdutos.html", produtos = _lista, content_type='application/json')

@bp_produto.route("/formProduto")
@validaSessao
def formProduto():
    produto = Produtos()
    return render_template("formProduto.html", produto=produto, content_type='application/json')

@bp_produto.route("/formEditProduto", methods = ['POST'])
@validaSessao
def formEditProduto():
    produto = Produtos()
    produto.id_produto = request.form['id_produto']
    produto.selectONE()
    return render_template('formProduto.html', produto=produto, content_type='application/json')

@bp_produto.route("/addProduto", methods = ['POST'])
@validaSessao
def addProduto():
    try:
        
        _produto = Produtos()
        _produto.descricao = request.form['descricao']
        _produto.valor = request.form['valor']
        _produto.imagem = "data:" + request.files['imagem'].content_type + ";base64," + str(base64.b64encode(request.files['imagem'].read()), "utf-8")

        _mensagem = _produto.insert()

        return jsonify(erro = False, mensagem = _mensagem)

    except Exception as e:
        if len(e.args)> 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)


@bp_produto.route("/editProduto", methods=['POST'])
@validaSessao
def editProduto():
    _mensagem = ""
    try:
        produto = Produtos()
        produto.id_produto = request.form['id_produto']
        produto.descricao = request.form['descricao']
        produto.valor = request.form['valor']
        produto.imagem = "data:" + request.files['imagem'].content_type + ";base64," + str(base64.b64encode(request.files['imagem'].read()), "utf-8")

        _mensagem = produto.update()
        return jsonify(erro=False, mensagem=_mensagem)
    except Exception as e:
        if len(e.args)> 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)

@bp_produto.route("/deleteProduto", methods=['POST'])
@validaSessao
def deleteProduto():
    _msg = ""
    try:
        _produto = Produtos()
        _produto.id_produto = request.form['id_produto']
        _msg = _produto.delete()
        return jsonify(erro=False, mensagem=_msg)
    except Exception as e:
        if len(e.args)> 1:
            _mensagem, _mensagem_exception = e.args
        else:
            _mensagem = 'Erro no banco'
            _mensagem_exception = e.args
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)

@bp_produto.route('/pdfProduto', methods=['POST'])
@validaSessao
def pdfProduto():
    geraPdf = PDF()
    geraPdf.pdfProdutos()
    return send_file('pdfProdutos.pdf', attachment_filename='pdfProdutos.pdf')