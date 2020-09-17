#coding utf-8
from flask import Flask, render_template
from mod_cliente.cliente import bp_cliente
from mod_produto.produto import bp_produto
from mod_home.home import bp_home
from mod_pedido.pedido import bp_pedido
from mod_erro.erro import bp_erro

app = Flask(__name__)
app.register_blueprint(bp_cliente)
app.register_blueprint(bp_produto)
app.register_blueprint(bp_home)
app.register_blueprint(bp_pedido)
app.register_blueprint(bp_erro)

@app.errorhandler(404)
def nao_encontrado(error):
    return render_template("form404.html"), 404

@app.errorhandler(500)
def erro_servidor(error):
    return render_template("form500.html"), 500
if __name__ == "__main__":
    app.run()
