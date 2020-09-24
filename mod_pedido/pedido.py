#coding: utf-8
from flask import Blueprint, render_template, request
from mod_login.login import validaSessao

bp_pedido = Blueprint('pedidos',__name__, url_prefix='/pedidos', template_folder='templates')

@bp_pedido.route("/")
@validaSessao
def formListaPedidos():
    return render_template("formListaPedidos.html")

@bp_pedido.route("/formPedido")
@validaSessao
def formPedido():
    return render_template("formPedido.html")