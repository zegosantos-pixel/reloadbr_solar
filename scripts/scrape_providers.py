
"""Template scraper: configure SOURCES with url+parser name. Adjust parsing functions.
Respect robots.txt and site's TOS. Output saved to static/data/empresas.json"""
from bs4 import BeautifulSoup
import requests, json, os, time

SOURCES = [
    # {"url":"https://example.com/planos","parser":"example_parser"}
]

OUT = os.path.join('static','data','empresas.json')

def example_parser(html):
    soup = BeautifulSoup(html,'html.parser')
    items = []
    for card in soup.select('.provider-card')[:20]:
        nome = card.select_one('.provider-name').get_text(strip=True)
        preco = card.select_one('.price').get_text(strip=True)
        preco = float(preco.replace('R$','').replace(',','.').strip())
        estado = card.select_one('.coverage').get_text(strip=True)[:2].upper()
        items.append({'nome':nome,'estado':estado,'preco_kwh':preco,'beneficios':'','site':''})
    return items

def fetch_and_parse(s):
    try:
        r = requests.get(s['url'], timeout=15, headers={'User-Agent':'reloadbrbot/1.0'})
        r.raise_for_status()
        if s.get('parser')=='example_parser':
            return example_parser(r.text)
    except Exception as e:
        print('Erro',e)
    return []

def main():
    all_items=[]
    for s in SOURCES:
        items = fetch_and_parse(s)
        all_items.extend(items)
        time.sleep(1.5)
    # dedupe by nome+estado
    seen=set(); out=[]
    for it in all_items:
        key=(it.get('nome'),it.get('estado'))
        if key not in seen:
            seen.add(key); out.append(it)
    with open(OUT,'w',encoding='utf-8') as f:
        json.dump(out,f,ensure_ascii=False,indent=2)
    print('Saved',len(out),'providers to',OUT)

if __name__=='__main__':
    main()
