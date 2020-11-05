#coding utf-8
from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import hashlib


from mod_cliente.clienteBD import Clientes
from funcoes import Funcoes

bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')



# valida se o usuário esta ativo na sessão
def validaSessao(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            #descarta os dados copiados da função original e retorna a tela de login
            return redirect(url_for('login.login', falhaSessao=1))
        else:
            #retorna os dados copiados da função original
            return f(*args, **kwargs)

    #retorna o resultado do if acima
    return decorated_function

@bp_login.route("/")
def login():
    return render_template('formLogin.html')

@bp_login.route("/logoff")
def logoff():

    Funcoes.criaLOG('Logoff', 'info')
    session.clear()    
    return redirect(url_for('login.login'))

@bp_login.route("/login", methods=['POST'])
def validaLogin():
    cliente = Clientes()
    _name = request.form['usuario']
    _pass = request.form['senha']

    cliente.login = _name
    cliente.senha = Funcoes.criptografaSenha(_pass)

    try:
        cliente.selectLogin()

        if cliente.id_cliente > 0:
            #limpa a sessão
            session.clear()

            #inclui o nome do usuário na sessão
            session['usuario'] = cliente.nome
            session['login'] = cliente.login
            session['grupo'] = cliente.grupo

            Funcoes.criaLOG('Login', 'info')

            
            return jsonify(erro = False, mensagem = f'Bem vindo {cliente.nome}!')
        else:
            
            return jsonify(erro = True, mensagem = "Usuário ou senha incorretos!")
    except Exception as e:
        _mensagem, _mensagem_exception = e.args
        Funcoes.criaLOG(f'{_mensagem} Excecao: {_mensagem_exception}', 'error')
        return jsonify(erro = True, mensagem = _mensagem, mensagem_exception = _mensagem_exception)

