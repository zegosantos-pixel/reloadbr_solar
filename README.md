ReloadBR Solar - Pacote Fullstack (versão unificada)
====================================================

O pacote contém um backend Flask com SQLAlchemy, templates com Tailwind, um scraper template,
Dockerfile/docker-compose para rodar com PostgreSQL, e um scaffold React opcional.

Instruções rápidas:
- Substitua backend/static/img/logo.png pela sua logo (mesmo nome).
- Para testar local (sem docker):
    cd <pasta-do-pacote>
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python backend/app.py
    Acesse http://127.0.0.1:5000
- Para rodar com docker-compose:
    docker-compose up --build
- Para deploy no Render: conecte o repo e aponte para iniciar gunicorn backend.app:app

Observações:
- O scraper é um template e precisa de parsers para cada site.
- Coletar dados de sites requer atenção a robots.txt e termos de uso.
