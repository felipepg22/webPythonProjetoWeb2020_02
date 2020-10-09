# coding utf-8
from flask import Blueprint, render_template, request, url_for, redirect, jsonify

from mod_login.login import validaSessao
from mod_cliente.clienteBD import Clientes

bp_cliente = Blueprint('cliente', __name__, url_prefix='/cliente', template_folder='templates')

@bp_cliente.route("/", methods=['GET', 'POST'])
@validaSessao
def formListaClientes():
    cliente = Clientes()
    res = cliente.selectAll()
    return render_template("formListaClientes.html", result=res, content_type='application/json')


@bp_cliente.route("/formCliente")
@validaSessao
def formCliente():
    cliente = Clientes()    
    return render_template("formCliente.html", cliente=cliente, content_type='application/json')
    

@bp_cliente.route("/formEditCliente", methods=['POST'])
@validaSessao
def formEditCliente():
    cliente = Clientes()
    cliente.id_cliente = request.form['id_cliente']
    cliente.selectOne()
    return render_template('formCliente.html', cliente=cliente, content_type='application/json')

@bp_cliente.route("/addCliente", methods = ['POST'])
@validaSessao
def addCliente():
    _mensagem = ""    
    try:
        cliente = Clientes()
        cliente.id_cliente = request.form['id_cliente']    
        cliente.nome = request.form['nome']
        cliente.endereco = request.form['endereco']
        cliente.numero = request.form['numero']
        cliente.observacao = request.form['observacao']
        cliente.cep = request.form['cep']
        cliente.bairro = request.form['bairro']
        cliente.cidade = request.form['cidade']
        cliente.estado = request.form['estado']
        cliente.telefone = request.form['telefone']
        cliente.email = request.form['email']
        cliente.login = request.form['login']
        cliente.senha = request.form['senha']
        cliente.grupo = request.form['grupo']
        _mensagem = cliente.insert()
        return jsonify(erro = False, mensagem = _mensagem)
    except:
        return jsonify(erro = True, mensagem = _mensagem)
    
    

@bp_cliente.route("/editCliente", methods=['POST'])
@validaSessao
def editCliente():
    try:
        cliente = Clientes()
        cliente.id_cliente = request.form['id_cliente']
        tipo = request.form['tipo']
        
       
        if tipo == 'editar':
            cliente.nome = request.form['nome']
            cliente.endereco = request.form['endereco']
            cliente.numero = request.form['numero']
            cliente.observacao = request.form['observacao']
            cliente.cep = request.form['cep']
            cliente.bairro = request.form['bairro']
            cliente.cidade = request.form['cidade']
            cliente.estado = request.form['estado']
            cliente.telefone = request.form['telefone']
            cliente.email = request.form['email']
            cliente.login = request.form['login']
            cliente.senha = request.form['senha']
            cliente.grupo = request.form['grupo']
            
            _mensagem = cliente.update()
        elif tipo == 'excluir':
            _mensagem = cliente.delete()

        return jsonify(erro = False, mensagem = _mensagem)
    except:
        return jsonify(erro = True, mensagem = _mensagem)