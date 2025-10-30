from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    empresas = [
        {"nome": "SunTech Solar", "preco_kwh": "0,72", "condicao": "Desconto médio 12%", "site": "https://suntechsolar.com.br"},
        {"nome": "Verde Energia", "preco_kwh": "0,68", "condicao": "Esperando para adesão", "site": "https://verdeenergia.com.br"},
        {"nome": "BluePower", "preco_kwh": "0,75", "condicao": "Programa de golden", "site": "https://bluepower.com.br"},
        {"nome": "EcoLuz Assinaturas", "preco_kwh": "0,70", "condicao": "Cashback 5%", "site": "https://ecoluz.com.br"},
    ]
    return render_template('index_full.html', empresas=empresas)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
