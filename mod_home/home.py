#coding: utf-8
from flask import Blueprint, render_template, request

bp_home = Blueprint('home', __name__, url_prefix="/home", template_folder='templates')

@bp_home.route("/")
def index():
    return render_template("home.html")