import json
from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# --- Caminho para o arquivo JSON com os dados das empresas ---
DATA_PATH = os.path.join(app.static_folder, 'data', 'empresas.json')


def carregar_empresas():
    """
    Lê os dados do arquivo empresas.json, faz a ordenação por preço (crescente)
    e relevância. Se o arquivo não for encontrado, retorna dados fictícios.
    """
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            empresas = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Caso o arquivo não exista ou esteja com erro, usa dados padrão
        empresas = [
            {"nome": "SunTech Solar", "preco_kwh": 0.72, "condicao": "Desconto médio 12%", "site": "https://suntechsolar.com.br", "relevancia": 8.9},
            {"nome": "Verde Energia", "preco_kwh": 0.68, "condicao": "Espera para adesão", "site": "https://verdeenergia.com.br", "relevancia": 9.2},
            {"nome": "BluePower", "preco_kwh": 0.75, "condicao": "Programa de fidelidade", "site": "https://bluepower.com.br", "relevancia": 8.3},
            {"nome": "EcoLuz Assinaturas", "preco_kwh": 0.70, "condicao": "Cashback 5%", "site": "https://ecoluz.com.br", "relevancia": 8.5},
        ]

    # Ordena por preço (menor primeiro), depois por relevância (maior primeiro)
    empresas.sort(key=lambda e: (e["preco_kwh"], -e["relevancia"]))
    return empresas


@app.route('/')
def index():
    empresas = carregar_empresas()
    return render_template('index.html', empresas=empresas)


# --- Estrutura futura para scraping automatizado (ainda desativada) ---
"""
@app.route('/atualizar')
def atualizar_empresas():
    from scraping import coletar_dados
    novas_empresas = coletar_dados()
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(novas_empresas, f, ensure_ascii=False, indent=4)
    return "Dados atualizados!"
"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

