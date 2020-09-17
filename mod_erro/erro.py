#coding: utf-8
from flask import Blueprint, render_template

bp_erro = Blueprint('erro',__name__, url_prefix='/', template_folder='templates')

@bp_erro.errorhandler(404)
def form_404(error):
    return render_template("form404.html"), 404

@bp_erro.errorhandler(500)
def form_500(error):
    return render_template("form500.html"), 500