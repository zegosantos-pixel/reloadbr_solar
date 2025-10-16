
ReloadBR Solar - Versão de Revisão (nome do ZIP: reloadbr_solar.zip)
==================================================================

Conteúdo:
- app.py                   : aplicativo Flask (lê static/data/empresas.json)
- templates/index.html     : front-end com Tailwind (CDN) e fonte Inter
- static/img/logo.png      : placeholder; substitua por sua logo (mesmo nome)
- static/data/empresas.json: base de dados inicial (exemplo)
- scripts/scrape_providers.py : modelo de scraper para coletar dados reais
- requirements.txt, Procfile, render.yaml : prontos para deploy no Render

Como usar (local):
1. Substitua static/img/logo.png pela sua logo (mesmo nome).
2. Crie e ative virtualenv:
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
3. Instale dependências:
   pip install -r requirements.txt
4. (Opcional) Rode o scraper depois de configurar SOURCES:
   python scripts/scrape_providers.py
   Isso atualizará static/data/empresas.json com dados coletados.
   Respeite robots.txt e termos dos sites.
5. Rode o app:
   python app.py
   Acesse http://127.0.0.1:5000

Como enviar mantendo o commit inicial:
git add -A
git commit --amend -m "Primeira versão do ReloadBR Solar"
git push --force origin main

Scraping legal/ética:
- Sempre verifique robots.txt e termos de uso.
- Use intervalos (sleep) entre requests e identifique User-Agent.
- Prefira APIs oficiais quando disponíveis.
