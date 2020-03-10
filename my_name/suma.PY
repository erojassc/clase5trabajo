from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def suma():   
    valor1 = request.args.get("valor1","0")
    valor2 = request.args.get("valor2","0")
    return f'La suma es , {escape((int(valor1)+int(valor2)))}!'