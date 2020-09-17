#coding utf-8
from flask import Flask, render_template
from mod_cliente.cliente import bp_cliente

app = Flask(__name__)
app.register_blueprint(bp_cliente)

@app.route("/")
def index():
    return render_template("modelo.html")


if __name__ == "__main__":
    app.run()
