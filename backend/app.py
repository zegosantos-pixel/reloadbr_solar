import os
from flask import Flask, render_template, request, jsonify, send_from_directory
import json
from datetime import datetime
from backend.models import db, Provider

app = Flask(__name__, template_folder='templates', static_folder='static')
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///reloadbr.db')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET'])
def index():
    return render_template('index_full.html', current_year=datetime.now().year)

@app.route('/api/providers', methods=['GET'])
def api_providers():
    estado = request.args.get('estado', '').upper()
    q = Provider.query
    if estado:
        q = q.filter(Provider.estado==estado)
    q = q.order_by(Provider.preco_kwh.asc(), Provider.relevancia.desc())
    providers = [p.to_dict() for p in q.limit(200).all()]
    return jsonify(providers)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
