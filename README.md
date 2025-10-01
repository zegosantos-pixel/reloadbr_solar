# ReloadBR Solar
Mini-site estilo Trivago para comparar empresas de energia solar por assinatura.

## Como usar localmente
1. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Rode o servidor:
   ```bash
   python app.py
   ```
3. Acesse em `http://127.0.0.1:5000`

## Deploy no Render
- Crie repositório no GitHub com esses arquivos.
- Conecte ao Render e escolha "Deploy from GitHub".
- Ele detecta Flask automaticamente.

## Estrutura de dados
- `data/solar_providers.csv` contém a base de provedores de energia solar por assinatura.
