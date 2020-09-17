#coding: utf-8
from flask import Blueprint, render_template, request

bp_pedido = Blueprint('pedidos',__name__, url_prefix='/pedidos', template_folder='templates')

@bp_pedido.route("/")
def formListaPedidos():
    return render_template("formListaPedidos.html")

@bp_pedido.route("/formPedido")
def formPedido():
    return render_template("formPedido.html")