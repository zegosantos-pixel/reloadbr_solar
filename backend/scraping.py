import json
import os
import requests
from bs4 import BeautifulSoup
import threading
import time

# Caminho do arquivo JSON de empresas
DATA_PATH = os.path.join(os.path.dirname(__file__), 'static', 'data', 'empresas.json')

def coletar_empresas():
    """
    Coleta ou simula a coleta de dados de empresas de energia solar no Brasil.
    """
    try:
        url = "https://www.portal-energia.com/empresas-energia-solar-brasil/"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        empresas = []

        for li in soup.select('ul li'):
            nome = li.get_text(strip=True)
            if nome:
                empresas.append({
                    "nome": nome,
                    "site": "",
                    "plano": "Sob consulta",
                    "preco": "",
                    "avaliacao": "",
                    "relevancia": 0
                })

        if not empresas:
            # fallback: usa dados locais
            if os.path.exists(DATA_PATH):
                with open(DATA_PATH, 'r', encoding='utf-8') as f:
                    empresas = json.load(f)
            else:
                empresas = [{
                    "nome": "Exemplo Solar",
                    "site": "",
                    "plano": "Residencial",
                    "preco": "R$ 299/mês",
                    "avaliacao": "4.5",
                    "relevancia": 1
                }]

        with open(DATA_PATH, 'w', encoding='utf-8') as f:
            json.dump(empresas, f, indent=4, ensure_ascii=False)

        print(f"{len(empresas)} empresas atualizadas e salvas em empresas.json")

    except Exception as e:
        print("Erro ao coletar dados:", e)

def agendar_atualizacao(intervalo_horas=168):
    """
    Agenda atualização semanal dos dados (padrão: 168h = 7 dias).
    """
    def tarefa():
        while True:
            print("🔄 Atualizando dados de empresas...")
            coletar_empresas()
            time.sleep(intervalo_horas * 3600)  # converte horas em segundos

    thread = threading.Thread(target=tarefa, daemon=True)
    thread.start()
