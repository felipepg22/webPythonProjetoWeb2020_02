#coding: utf-8
from flask import Blueprint, render_template

bp_erro = Blueprint('erro',__name__, url_prefix='/', template_folder='templates')

@bp_erro.app_errorhandler(404)
def erro404(error):
    return render_template("form404.html")


@bp_erro.app_errorhandler(500)
def erro500(error):
    return render_template("form500.html")