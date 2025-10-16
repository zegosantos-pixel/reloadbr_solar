
import os
from flask import Flask, render_template, request, send_from_directory
import json
from datetime import datetime

app = Flask(__name__)

PRIMARY_DATA = os.path.join('static', 'data', 'empresas.json')
FALLBACK_DATA = os.path.join('static', 'data', 'empresas_fallback.json')

def load_empresas():
    path = PRIMARY_DATA if os.path.exists(PRIMARY_DATA) else FALLBACK_DATA
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print('Erro ao carregar dados:', e)
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    estado = ''
    empresas = []
    if request.method == 'POST':
        estado = request.form.get('estado','').strip().upper()
        todas = load_empresas()
        filtradas = [e for e in todas if (not estado) or e.get('estado','').upper() == estado]
        try:
            empresas = sorted(filtradas, key=lambda x: float(x.get('preco_kwh') or 9999))
        except Exception:
            empresas = filtradas
    return render_template('index.html', empresas=empresas, estado=estado, current_year=datetime.now().year)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
