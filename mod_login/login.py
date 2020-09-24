#coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for, session

bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')

@bp_login.route("/")
def login():
    return render_template('formLogin.html')

@bp_login.route("/logoff")
def logoff():
    session.clear()
    return redirect(url_for('login.login'))

@bp_login.route("/login", methods=['POST'])
def validaLogin():
    _name = request.form['usuario']
    _pass = request.form['senha']

    if _name == 'abc' and _pass == 'Bolinhas':
        #limpa a sessão
        session.clear()

        #inclui o nome do usuário na sessão
        session['usuario'] = _name

        #abre a aplicação na tela home
        return redirect(url_for('home.index'))
    else:
        #retorna para a tela de login
        return redirect(url_for('login.login', falhaLogin=1))