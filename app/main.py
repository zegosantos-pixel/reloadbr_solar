
from flask import Flask, render_template, request
import json, os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar')
def buscar():
    estado = request.args.get('estado', '').upper()
    with open(os.path.join('app', 'data', 'empresas.json'), 'r', encoding='utf-8') as f:
        dados = json.load(f)
    resultados = [x for x in dados if x['estado'] == estado] if estado else []
    return render_template('index.html', resultados=resultados, estado=estado)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
