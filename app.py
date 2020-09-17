#coding utf-8
from flask import Flask, render_template
from mod_cliente.cliente import bp_cliente
from mod_produto.produto import bp_produto

app = Flask(__name__)
app.register_blueprint(bp_cliente)
app.register_blueprint(bp_produto)

@app.route("/")
def index():
    return render_template("modelo.html")


if __name__ == "__main__":
    app.run()
