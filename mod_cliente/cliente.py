# coding utf-8
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, send_file
import hashlib

from mod_login.login import validaSessao
from mod_cliente.clienteBD import Clientes
from funcoes import Funcoes
from classeGeraPdf import PDF

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
        cliente.senha = Funcoes.criptografaSenha(request.form['senha'])
        cliente.grupo = request.form['grupo']
        _mensagem = cliente.insert()
        return jsonify(erro = False, mensagem = _mensagem)
    except Exception as e:
        if len(e.args) > 1:
            _mensagem, _mensagem_exception = e.args
            return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)
        else:
            return jsonify(erro = True,mensagem = "Erro ao tentar cadastrar cliente!" ,mensagem_exception = str(e))
    
    

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
            cliente.grupo = request.form['grupo']
            
            _mensagem = cliente.update()
        elif tipo == 'excluir':
            _mensagem = cliente.delete()

        return jsonify(erro = False, mensagem = _mensagem)
    except Exception as e:
        _mensagem, _mensagem_exception = e.args
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)

@bp_cliente.route('/verificaSeLoginExiste', methods = ['POST'])
@validaSessao
def verificaSeLoginExiste():
    cliente = Clientes()
    cliente.login = request.form['login']

    try:
        result = cliente.verificaSeLoginExiste()
        #Verifica se achou o login no banco
        if len(result) > 0:
            return jsonify(login_existe = True)
        else:
            return jsonify(login_existe = False)
    except Exception as e:
        return jsonify(erro = True, mensagem_exception = str(e))

@bp_cliente.route('/pdfCliente', methods=['POST'])
@validaSessao
def pdfCliente():
    geraPdf = PDF()
    geraPdf.pdfClientes()
    return send_file('pdfClientes.pdf', attachment_filename='pdfClientes.pdf')